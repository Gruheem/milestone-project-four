
import stripe
import json

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from profiles.models import UserProfile

from .forms import OrderForm
from bag.contexts import bag_contents
from .models import Order

stripe_client = stripe.StripeClient(settings.STRIPE_SECRET_KEY)

# Create your views here.
def checkout(request):  
    """ A view to return the checkout page """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag')
        return redirect(reverse('products'))

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.default_full_name,
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'checkout/checkout.html', context)


@require_POST
def create_checkout_session(request):
    """
    Validates the OrderForm, converts bag contents into stripe format and creates a stripe checkout session.s
    """
    # Check whether the bag exists 
    bag = request.session.get('bag', {})
    if not bag:
        return JsonResponse({'error': 'Your bag is empty'}, status=400)

    # Validates the content of the form so we know its trustworthy before giving it to stripe
    order_form = OrderForm(request.POST)
    if not order_form.is_valid():
        return JsonResponse({'error': order_form.errors}, status=400)

    current_bag = bag_contents(request)

    # Turns the items in the bag into items that stripe can understand using the 'price_data' dictionary nested in the 'line_items' list. 
    line_items = []
    for item in current_bag['bag_items']:
        product = item['product']
        line_items.append({
            'price_data': {
                'currency': 'gbp',
                'product_data': {'name': product.product_name},
                'unit_amount': round(product.price * 100),
            },
            'quantity': item['quantity'],
        })

    # Adds Delivery to the total done here as it is not a product in the bag
    delivery = current_bag['delivery']
    if delivery > 0:
        line_items.append({
            'price_data': {
                'currency': 'gbp',
                'product_data': {'name': 'Delivery'},
                'unit_amount': round(delivery * 100),
            },
            'quantity': 1,
        })

    # Creates a checkout session 
    session = stripe_client.v1.checkout.sessions.create(
        params={
            'line_items': line_items,
            'mode': 'payment',
            'ui_mode': 'elements',
            # The return url is where the user will be redirected to after they have completed their payment.
            'return_url': (
                request.build_absolute_uri(reverse('checkout_return'))
                + '?session_id={CHECKOUT_SESSION_ID}'
            ),
            'customer_email': order_form.cleaned_data['email'],
            # This meta data is 'packed' into string format for us to unpack when we recieve the payment webhook from stripe
            'metadata': {
                'bag': json.dumps(bag),
                'order_form': json.dumps(order_form.cleaned_data),
                'save_info': request.POST.get('save-info', ''),
                'username': str(request.user) if request.user.is_authenticated else 'AnonymousUser',
            },
        },
    )

    return JsonResponse({'clientSecret': session.client_secret})


def checkout_return(request):
    '''
    A view to handle the return from stripe after a successful payment for a summary.
    '''
    # Retrieve the session_id from the query parameters and use it to retrieve the session object from Stripe
    session_id = request.GET.get('session_id')
    session = stripe_client.v1.checkout.sessions.retrieve(session_id)

    if session.status != 'complete':
        messages.error(
            request,
            'Your payment did not go through, please try again.'
        )
        return redirect(reverse('checkout'))

    try:
        order = Order.objects.get(
            stripe_pid=session.payment_intent
        )
    except Order.DoesNotExist:
        return render(
            request,
            'checkout/checkout_return.html',
            {'payment_intent': session.payment_intent}
        )

    # Delete the bag as it has been fulfilled
    if 'bag' in request.session:
        del request.session['bag']

    return render(
        request,
        'checkout/checkout_success.html',
        {'order': order}
    )


def check_order(request):
    payment_intent = request.GET.get('payment_intent')

    if not payment_intent:
        return JsonResponse(
            {'error': 'Missing payment intent'},
            status=400
        )

    try:
        order = Order.objects.get(
            stripe_pid=payment_intent
        )
    except Order.DoesNotExist:
        return JsonResponse({'ready': False})

    return JsonResponse({
        'ready': True,
        'order_number': order.order_number,
    })
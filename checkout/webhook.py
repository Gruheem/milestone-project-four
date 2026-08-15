import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .webhook_handler import StripeWH_Handler


@csrf_exempt
def webhook(request):

    stripe_client = stripe.StripeClient(settings.STRIPE_SECRET_KEY)
    wh_secret = settings.STRIPE_WH_SECRET

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        # Confirm with our wh-secret that the webhook is from Stripe and not a fraudulent request
        event = stripe_client.construct_event(payload, sig_header, wh_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    # Assign a handler to the webhook event
    handler = StripeWH_Handler(request)
    # Map the webhook events to the relevant handler functions
    event_map = {
        'checkout.session.completed': handler.handle_checkout_session_completed,
        'checkout.session.expired': handler.handle_checkout_session_expired,
    }

    # Get the relevant handler function based on the event type as described in the event map dictionary, or use the generic handler if not found
    event_handler = event_map.get(event['type'], handler.handle_event)
    return event_handler(event)
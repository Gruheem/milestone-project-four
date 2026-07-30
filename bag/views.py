from django.shortcuts import redirect, render

# Create your views here.
def view_bag(request):
    ''' A view to return the bag page '''

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' Add a quantity of the specified product to the shopping bag '''

    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    print(request.session['bag'])
    return redirect(redirect_url)
    
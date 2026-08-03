from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def view_bag(request):
    ''' A view to return the bag page '''

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' Add a quantity of the specified product to the shopping bag '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})


    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    ''' Adjust the quantity of the specified product in the shopping bag '''

    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity >= 1:
        bag[item_id] = quantity
    

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))    


def remove_from_bag(request, item_id):
    ''' Remove the specified product from the shopping bag '''

    bag = request.session.get('bag', {})

    # Convert item_id into a string to match the data stored in the sessions bag dictionary
    item_id = str(item_id)

    if item_id in bag:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))  

    
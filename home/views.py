from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def test_404(request):
    return render(request, "home/test-404.html")
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def trackOrder(request):
    return render(request, 'trackOrder.html')
def about(request):
    return render(request, 'about.html')
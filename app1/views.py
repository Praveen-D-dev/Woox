from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render (request, 'index.html')

def about(request):
    return render(request, 'about.html')

def deals(request):
    return render(request, 'deals.html')

def reservation(request):
    return render(request, 'reservation.html')
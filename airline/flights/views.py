from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        "flights": flights,
        })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
    })
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CodeForm
from .models import Flight  # Import Flight model
from airports.models import Airport  # Import airport model to get airport id and code


def index(request):
    form = CodeForm()
    return render(request, "flights/index.html", {'form': form})


def search(request):
    form = CodeForm(request.POST)
    if form.is_valid():
        flights = Flight.objects.filter(origin__airport_code=form.cleaned_data['origin'],
                                        destination__airport_code=form.cleaned_data['destination'])

        return render(request, 'flights/flights_search.html', {'flights': flights})


def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    # Code to select flights from the database
    flights = Flight.objects.filter(origin_id=origin, destination_id=destination)
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)

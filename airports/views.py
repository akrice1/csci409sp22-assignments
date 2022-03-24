from django.http import HttpResponse
from django.shortcuts import render  # Import the render library to make loading templates easier.
from .models import Airport


def index(request):
    # Fetch all airports from database
    airports = Airport.objects.all()
    # Place all airports into a context variable for retrieval in the view.
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)


# Create your views here.
def airport_info(request, airport_code):
    # Fetch the airport by a certain code.
    # We are only expecting one airport per code so we will use get().
    airport = Airport.objects.get(airport_code=airport_code)
    context = {'airport': airport}
    return render(request, 'airports/airports.html', context)

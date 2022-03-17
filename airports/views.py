from django.http import HttpResponse
from .models import Airport
def index(request):
    # Fetch all airports from database
    airports = Airport.objects.all()
    # To show some data.
    airport_list = ', '.join([a.airport_code for a in airports])
    return HttpResponse('Showing all airports: ' + airport_list);

# Create your views here.
def airport_info(request, airport_code):
    # Fetch the airport by a certain code.
    # We are only expecting one airport per code so we will use get().
    airport = Airport.objects.get(airport_code=airport_code)
    # Display the airport name and code.
    return HttpResponse('Showing info for airport: ' + airport.name + "- " + airport.airport_code)



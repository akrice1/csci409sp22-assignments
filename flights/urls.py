from django.urls import path
# load this applications views.py file
from . import views

# define url patterns
urlpatterns = [
    path('/', views.index),
    path('/search/<str:origin>/<str:destination>/', views.flight_search),

]

from django.urls import path
# load this applications views.py file
from . import views

# define url patterns
urlpatterns = [
    path('/', views.index),
    path('/<int:confirmation_number>/', views.ticket_search),
    path('/search/', views.search),
]

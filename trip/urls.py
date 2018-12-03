from django.urls import path
from .views import *


urlpatterns = [
    path('addTrip', AddTrip.as_view()),
    path('getTripDetails', GetTripDetails.as_view()),
    path('getTripList', GetTripList.as_view()),
    path('deleteTrip', DeleteTrip.as_view()),
    path('UpdateTrip', UpdateTrip.as_view()),
]

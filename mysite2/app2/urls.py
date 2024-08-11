from django.urls import path
from . import views

urlpatterns = [
    path('trains', views.trains,name="trainspage"),
    path('hotel', views.hotel,name="hotelpage"),
    path('flights', views.flights,name="flightspage"),
    path('bus', views.bus,name="buspage"),
    path('home/<int:num>', views.home,name="homepage"),
    path('home/<int:num>', views.home,name="homepage"),
    path('contact', views.contact,name="contactpage"),
    path('<str:hero>', views.actor),
    path('', views.search,name="searchpage"),
]
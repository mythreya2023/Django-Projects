from django.urls import path
from clgEvents import views

urlpatterns=[
    path("",views.displayEve,name="EventsPage"),
    path("create",views.createEve,name="CreateEventPage"),
]


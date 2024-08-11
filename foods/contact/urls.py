from django.urls import path
from contact import views

urlpatterns = [
    path('admin', views.notifyAdmin, name='contact'),
    path('user', views.notifyUser, name='notify'),
]
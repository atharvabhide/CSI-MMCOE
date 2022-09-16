from django.urls import path
from . import views

urlpatterns = [
    path('events', views.event, name='events'),
    path('current_event', views.currEvent, name='current_event'),
    path('contact', views.contactUs, name='contact'),
]
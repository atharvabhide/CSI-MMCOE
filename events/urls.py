from django.urls import path
from . import views

urlpatterns = [
    path('events', views.event, name='events'),
    path('special_events', views.spEvent, name='special_events'),
    path('contact_us', views.contactUs, name='contact_us'),
]
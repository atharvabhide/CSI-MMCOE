from django.shortcuts import render
from .models import csi_Event

def event(request):
    events_list = list(csi_Event.objects.all())
    return render(request, 'events.html', { 'events_list' : events_list })

def spEvent(request):
    curr_event = list(csi_Event.objects.all())[-1]
    return render(request, 'special_events.html', { 'curr_event' : curr_event })

def contactUs(request):
    return render(request, 'contact_us.html')
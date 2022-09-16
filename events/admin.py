from django.contrib import admin
from .models import csi_Event
# Register your models here.

@admin.register(csi_Event)
class csi_eventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_description')
    search_fields = ('event_name', 'event_description')
from django.contrib import admin
from django.forms import forms
from .models import Event, EventTicket, Speaker

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    search_fields = ('name',)


@admin.register(EventTicket)
class EventTicketAdmin(admin.ModelAdmin):
    model = EventTicket


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    model = Speaker
    filter_horizontal = ("events",)
    search_fields = ('name', 'events__name')

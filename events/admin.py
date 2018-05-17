from django.contrib import admin
from .models import Event, EventTicket

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event


@admin.register(EventTicket)
class EventTicketAdmin(admin.ModelAdmin):
    model = EventTicket

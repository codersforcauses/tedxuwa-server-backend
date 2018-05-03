from django.contrib import admin
from .models import Event, EventSignup

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event


@admin.register(EventSignup)
class EventSignupAdmin(admin.ModelAdmin):
    model = EventSignup

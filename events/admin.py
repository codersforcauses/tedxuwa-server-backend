from django.contrib import admin
from django.forms import forms
from .models import Event, EventTicket, Speaker, Talk

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    search_fields = ("name",)
    list_filter = ("event_type", "featured")
    list_display = ("__str__", "published", "featured")
    list_editable = ("published", "featured")


@admin.register(EventTicket)
class EventTicketAdmin(admin.ModelAdmin):
    model = EventTicket


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    model = Speaker
    filter_horizontal = ("events",)
    search_fields = ("name", "events__name")


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    model = Talk
    list_filter = ("event",)
    search_fields = ("event", "speaker", "title", "link")

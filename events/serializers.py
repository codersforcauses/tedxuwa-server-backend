from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "event_type", "name", "description", "location",
                  "start", "end", "banner_image", "ticket_url")

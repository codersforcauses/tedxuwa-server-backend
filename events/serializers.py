from rest_framework import serializers
from .models import Event, Speaker


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "event_type", "name", "description", "location",
                  "start", "end", "banner_image", "featured", "ticket_url")


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ("id", "event", "name", "profile_image",
                  "bio")

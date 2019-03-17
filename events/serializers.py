from rest_framework import serializers
from .models import Event, Speaker, Talk


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "event_type", "name", "description", "location",
                  "start", "end", "banner_image", "featured", "ticket_url")


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ("id", "events", "name", "profile_image",
                  "tag_line", "bio")


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ("id", "event", "speaker", "title", "link")

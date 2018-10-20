from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .models import Event, Speaker
from .serializers import EventSerializer, SpeakerSerializer

# Create your views here.


class EventViewSet(ReadOnlyModelViewSet):
    # only allow listing and fetching single
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SpeakerViewset(ListAPIView):
    # only allow listing and fetching single
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        event = get_object_or_404(Event, id=self.kwargs.get("event_id"))
        return event.speakers.all()

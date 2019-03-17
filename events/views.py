from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .models import Event, Speaker, Talk
from .serializers import EventSerializer, SpeakerSerializer, TalkSerializer

# Create your views here.


class EventViewSet(ReadOnlyModelViewSet):
    # only allow listing and fetching single
    queryset = Event.objects.filter(published=True)
    serializer_class = EventSerializer

    def get_queryset(self):
        # if "?featured" flag is present, only show featured events
        flags = self.request.query_params.dict().keys()
        if "featured" in flags:
            self.queryset = self.queryset.filter(featured=True)
        return self.queryset


class SpeakerViewSet(ListAPIView):
    # only allow listing and fetching single
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        event = get_object_or_404(Event, id=self.kwargs.get("event_id"))
        return event.speakers.all()


class TalkViewSet(ListAPIView):
    # only allow listing and fetching single
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

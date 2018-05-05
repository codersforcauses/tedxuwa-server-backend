from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

# Create your views here.


class EventViewSet(ReadOnlyModelViewSet):
    # only allow listing and fetching single
    queryset = Event.objects.all()
    serializer_class = EventSerializer

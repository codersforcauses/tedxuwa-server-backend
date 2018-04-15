from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Event
from .serializers import EventSerializer

# Create your views here.


class EventViewSet(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

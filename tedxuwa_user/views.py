from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from .models import Member
from .serializers import MemberSerializer

# Create your views here.


class ComitteeListView(ListAPIView):
    queryset = Member.objects.filter(is_comittee=True)
    serializer_class = MemberSerializer

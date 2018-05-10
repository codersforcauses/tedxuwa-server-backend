from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from .models import Member, CommitteeMember
from .serializers import MemberSerializer, CommitteeMemberSerializer

# Create your views here.


class CommitteeListView(ListAPIView):
    queryset = CommitteeMember.objects.all()
    serializer_class = CommitteeMemberSerializer

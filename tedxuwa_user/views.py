from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from .models import Member
from .serializers import MemberSerializer

# Create your views here.


class MemberListView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, member_type="current", *args, **kwargs):
        member_type = member_type.lower()
        if member_type == "current":
            self.queryset = self.queryset.filter(is_current=True)
        elif member_type == "past":
            self.queryset = self.queryset.filter(is_current=False)
        else:
            return Response({"status": "invalid member type, must be current or past"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(MemberListView, self).get(request, *args, **kwargs)

from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("id", "first_name", "last_name", "name",
                  "bio", "profile_picture_url", "is_current")

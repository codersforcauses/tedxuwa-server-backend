from rest_framework import serializers
from .models import Member, CommitteeMember


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("id", "first_name", "last_name", "name",
                  "profile_picture_url")


class CommitteeMemberSerializer(serializers.ModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = CommitteeMember
        fields = ("id", "member", "position", "bio", "linkedin_url")

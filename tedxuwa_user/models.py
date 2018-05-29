from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # extending abstract user for future expansion if necessary
    pass


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    profile_picture_url = models.URLField(blank=True, null=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def is_committee_member(self):
        # return whether or not this member is a committee member
        try:
            self.committee
            return True
        except CommitteeMember.DoesNotExist:
            return False

    def __str__(self):
        return self.name


class CommitteeMember(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE,
                                  related_name="committee")
    position = models.CharField(max_length=255)
    bio = models.TextField(blank=True, default="")
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{}:{}".format(
            self.position, self.member.__str__()
        )

    class Meta:
        ordering = ["order"]

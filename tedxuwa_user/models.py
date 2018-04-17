from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # extending abstract user for future expansion if necessary
    pass


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True, default="")
    profile_picture_url = models.URLField(blank=True, null=True)
    is_current = models.BooleanField(
        default=True, help_text="whether or not this member is a current comittee member")

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

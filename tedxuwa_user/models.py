from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # extending abstract user for future expansion if necessary
    pass

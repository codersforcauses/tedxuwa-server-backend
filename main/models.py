from django.db import models

# Create your models here.


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)
    logo_image = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

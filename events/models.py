from django.db import models

# Create your models here.


class Event(models.Model):
    SALON = "SALON"
    CONFERENCE = "CONFERENCE"
    WORKSHOP = "WORKSHOP"
    NETWORKING = "NETWORKING"
    OTHER = "OTHER"
    EVENT_TYPE_CHOCIES = (
        (SALON, "Salon"),
        (CONFERENCE, "Conference"),
        (WORKSHOP, "Workshop"),
        (NETWORKING, "Networking"),
        (OTHER, "Other"),
    )
    event_type = models.CharField(max_length=32,
                                  choices=EVENT_TYPE_CHOCIES,
                                  default=OTHER)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    banner_image = models.URLField(blank=True,
                                   help_text="link to the banner image file")
    ticket_url = models.URLField(blank=True)
    notes = models.TextField(blank=True, help_text="internal use only")

    def __str__(self):
        return self.name

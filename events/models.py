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
    start = models.DateTimeField(blank=True, null=True,
                                 help_text="Australia/Perth time")
    end = models.DateTimeField(blank=True, null=True,
                               help_text="Australia/Perth time")
    banner_image = models.URLField(blank=True,
                                   help_text="link to the banner image file")
    ticket_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    notes = models.TextField(blank=True, help_text="internal use only")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EventTicket(models.Model):
    """Keep track of who signed up for an event. Anyone who signed up for
    an event is automatically a member. Expand on this model as we get more
    analytics"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey("tedxuwa_user.Member", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1, help_text="how many tickets did they buy")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} x {}:{}".format(
            self.quantity, self.member.__str__(), self.event.__str__()
        )

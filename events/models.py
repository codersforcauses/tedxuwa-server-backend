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
    published = models.BooleanField(default=False,
                                    help_text="whether or not the event should be shown online")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-start"]


class EventTicket(models.Model):
    """Keep track of who signed up for an event. Anyone who signed up for
    an event is automatically a member. Expand on this model as we get more
    analytics"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey("tedxuwa_user.Member", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1, help_text="how many tickets did they buy")
    checked_in = models.BooleanField(default=False,
                                     help_text="whether or not they actually checked into the event")
    booking_method = models.CharField(blank=True, default="", max_length=255,
                                      help_text="how the person purchased the ticket")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} x {}:{}".format(
            self.quantity, self.member.__str__(), self.event.__str__()
        )


class Speaker(models.Model):
    events = models.ManyToManyField(Event, related_name="speakers",
                                    help_text="which event(s) this speaker is a part of")
    name = models.CharField(max_length=255)
    profile_image = models.URLField(blank=True)
    tag_line = models.CharField(max_length=255, blank=True,
                                default="")
    bio = models.TextField(blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Talk(models.Model):
    event = models.ForeignKey(Event, related_name="talks",
                              on_delete=models.CASCADE,
                              help_text="which event the talk as given at")
    speaker = models.ForeignKey(Speaker, related_name="talks",
                                on_delete=models.CASCADE,
                                help_text="which speaker gave this talk")
    title = models.CharField(max_length=1024)
    link = models.URLField()

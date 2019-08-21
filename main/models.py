from django.db import models

# Create your models here.


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)
    logo_image = models.URLField()
    link = models.URLField(blank=True)
    tier = models.IntegerField(default=3,
                               help_text="3 is the lowest and 1 is the highest where 3 = logo+description+link, 2 = logo+description and 1 = logo")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ForwardLink(models.Model):
    title = models.CharField(max_length=255,
                             help_text="title of the webpage, this will be shown on link previews")
    path = models.SlugField(
        max_length=255, help_text="the path for this url. The end result will be tedxuwa.com/r/PATH",
        unique=True)
    link = models.URLField(help_text="the link that this path leads to")

    @property
    def full_path(self):
        return "tedxuwa.com/r/" + self.path

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import Sponsor, ForwardLink

# Register your models here.


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    search_fields = ("name",)


@admin.register(ForwardLink)
class ForwardLinkAdmin(admin.ModelAdmin):
    model = ForwardLink
    search_fields = ("path", "title", "link")
    readonly_fields = ("full_path",)

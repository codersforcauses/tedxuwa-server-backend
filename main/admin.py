from django.contrib import admin
from .models import Sponsor

# Register your models here.


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    search_fields = ("name",)

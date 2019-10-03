from django.contrib import admin
from django.utils.html import mark_safe
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
    readonly_fields = ("full_path_link",)
    list_display = ("title", "full_path_link")

    def full_path_link(self, obj):
        return mark_safe('<a href="http://{}" target="_blank">{}</a>'.format(obj.full_path, obj.full_path))

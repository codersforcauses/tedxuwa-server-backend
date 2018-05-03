from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Member
from events.models import EventSignup


class EventSignupInline(admin.TabularInline):
    model = EventSignup
    extra = 0


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    model = Member
    inlines = [EventSignupInline]


admin.site.register(User, UserAdmin)

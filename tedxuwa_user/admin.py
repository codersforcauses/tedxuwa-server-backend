from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Member, CommitteeMember
from events.models import EventTicket


class EventTicketInline(admin.TabularInline):
    model = EventTicket
    extra = 0


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    model = Member
    inlines = [EventTicketInline]


@admin.register(CommitteeMember)
class MemberAdmin(admin.ModelAdmin):
    model = CommitteeMember


admin.site.register(User, UserAdmin)

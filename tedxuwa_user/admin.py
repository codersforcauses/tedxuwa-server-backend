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
    search_fields = ('first_name', 'last_name')


@admin.register(CommitteeMember)
class MemberAdmin(admin.ModelAdmin):
    model = CommitteeMember
    search_fields = ('member__first_name', 'member__last_name',
                     'position')


admin.site.register(User, UserAdmin)

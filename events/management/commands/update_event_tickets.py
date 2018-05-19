from django.core.management.base import BaseCommand, CommandError
from tedxuwa_user.models import Member
from events.models import EventTicket, Event

import csv


# define index numbers for the csv file here
FNAME = 1
LNAME = 0
EMAIL = 2
BOOKING_METHOD = 3
QUANTITY = 4
CHECKED_IN = 5


class Command(BaseCommand):
    help = "take in a json file of committee members and add them to the database"

    def add_arguments(self, parser):
        parser.add_argument("eventname", type=str)
        parser.add_argument("file", nargs="+")
        parser.add_argument("--ignorefirstline", nargs="?", default=False)

    def handle(self, *args, **options):
        event, c = Event.objects.get_or_create(
            name__icontains=options["eventname"],
            defaults={
                "name": options["eventname"]
            }
        )
        for path in options.get("file", []):
            linenum = 0
            with open(path, "r") as f:
                tickets = csv.reader(f)
                for ticket in tickets:
                    print(ticket)
                    if options["ignorefirstline"] and linenum == 0:
                        linenum += 1
                        continue
                    # heavy index assumptions
                    member, c = Member.objects.get_or_create(
                        first_name=ticket[FNAME],
                        last_name=ticket[LNAME],
                        email=ticket[EMAIL]
                    )
                    ti, c = EventTicket.objects.update_or_create(
                        member=member,
                        event=event,
                        defaults={
                            "quantity": ticket[QUANTITY],
                            "checked_in": True if str(ticket[CHECKED_IN]) == "1" else False,
                            "booking_method": ticket[BOOKING_METHOD]
                        }
                    )

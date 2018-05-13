from django.core.management.base import BaseCommand, CommandError

from events.models import Event

import json


class Command(BaseCommand):
    help = "take in a json file of events and add them to the database"

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="+")

    def handle(self, *args, **options):
        for path in options.get("files", []):
            data = json.load(open(path, "r"))
            for event in data:
                Event.objects.create(
                    event_type=event["type"].upper(),
                    name=event["title"],
                    description=event["description"],
                    banner_image=event["image"],
                    location=event["location"]
                )

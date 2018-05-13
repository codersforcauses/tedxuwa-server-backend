from django.core.management.base import BaseCommand, CommandError
from tedxuwa_user.models import Member, CommitteeMember

import json


class Command(BaseCommand):
    help = "take in a json file of committee members and add them to the database"

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="+")

    def handle(self, *args, **options):
        for path in options.get("files", []):
            data = json.load(open(path, "r"))
            for member in data:
                # must have name and position
                if member.get("name") is None:
                    print("skipping member without a name: {}".format(member))
                    continue
                elif member.get("position") is None:
                    print("skipping member without a position: {}".format(member))
                    continue
                # clean data
                names = member["name"].strip().split()
                fname = ""
                lname = ""
                if len(names) == 1:
                    fname = names[0]
                elif len(names) == 2:
                    fname = names[0]
                    lname = names[1]
                else:
                    # take everything else as last name
                    fname = names[0]
                    lname = " ".join(names[1:])
                # TODO parse links
                m, c = Member.objects.get_or_create(
                    first_name=fname,
                    last_name=lname,
                )
                if member.get("image"):
                    m.profile_picture_url = member["image"]
                    m.save()
                CommitteeMember.objects.get_or_create(
                    member=m,
                    defaults={
                        "position": member["position"]
                    }
                )

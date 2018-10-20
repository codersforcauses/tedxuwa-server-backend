from django.test import TestCase, Client
from events.models import Event

# Create your tests here.


class TestEventEndpoint(TestCase):
    fixtures = ["events/fixtures/events.json"]

    def setUp(self):
        self.c = Client()

    def test_endpoint(self):
        re = self.c.get("/api/events/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], 1)


class TestSpeakerEndpoint(TestCase):
    fixtures = ["events/fixtures/events.json",
                "events/fixtures/speakers.json"]

    def setUp(self):
        self.c = Client()
        self.event = Event.objects.first()

    def test_endpoint(self):
        re = self.c.get(f"/api/events/{self.event.id}/speakers/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], 1)
        # non existent event
        re = self.c.get("/api/events/000/speakers/")
        self.assertEqual(re.status_code, 404)

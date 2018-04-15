from django.test import TestCase, Client

# Create your tests here.


class TestEventEndpoint(TestCase):
    fixtures = ["events/fixtures/events.json"]

    def setUp(self):
        self.c = Client()

    def test_endpoint(self):
        re = self.c.get("/api/events/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], 1)

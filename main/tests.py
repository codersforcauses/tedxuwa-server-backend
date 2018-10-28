from django.test import TestCase, SimpleTestCase, Client
from .models import Sponsor

# Create your tests here.


class TestSponsorViewSet(TestCase):
    fixtures = ["main/fixtures/sponsors.json"]

    def setUp(self):
        self.c = Client()

    def test_view(self):
        re = self.c.get("/api/sponsors/")
        response = re.json()
        self.assertEqual(re.status_code, 200)
        self.assertEqual(response["count"],
                         Sponsor.objects.all().count())

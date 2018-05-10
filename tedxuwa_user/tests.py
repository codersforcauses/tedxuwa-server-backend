from django.test import TestCase, Client

from .models import Member
# Create your tests here.


class TestMemberEndpoint(TestCase):
    fixtures = ["tedxuwa_user/fixtures/members.json"]

    def setUp(self):
        self.c = Client()

    def test_endpoint(self):
        re = self.c.get("/api/committee/")
        self.assertEqual(re.status_code, 200)

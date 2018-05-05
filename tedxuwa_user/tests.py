from django.test import TestCase, Client

from .models import Member
# Create your tests here.


class TestMemberEndpoint(TestCase):
    fixtures = ["tedxuwa_user/fixtures/members.json"]

    def setUp(self):
        self.c = Client()
        # 2 members in the fixture, one present one not
        self.current_member = Member.objects.get(is_comittee=True)
        self.past_member = Member.objects.get(is_comittee=False)

    def test_endpoint(self):
        re = self.c.get("/api/committee/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], 1)
        # making both current members should return 0 past members
        self.past_member.is_comittee = True
        self.past_member.save()
        re = self.c.get("/api/committee/")
        self.assertEqual(re.status_code, 200)
        self.assertEqual(re.json()["count"], 2)

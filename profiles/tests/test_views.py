import pytest
from profiles.tests import factories
from django.test import TestCase
pytestmark = pytest.mark.django_db
from profiles.views import profile

class ProfilesTest(TestCase):
    
    def test_index_view(self):
        user1 = factories.UserFactory(username='test_user_1')
        user2 = factories.UserFactory(username='test_user_2')

        factories.ProfileFactory(user=user1)
        factories.ProfileFactory(user=user2)
        url = '/profiles/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_title(self):
        """Check if the title is OK"""
        response = self.client.get('/profiles/')
        self.assertContains(response, "profiles")

    def test_profile_view(self):
        user = factories.UserFactory(
            username='test_user',
            first_name='test_first_name',
            last_name='test_last_name',
            email='test_email_name',
        )
        factories.ProfileFactory(user=user)
        url = f"/profiles/{user.username}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = profile(self,user.username)
        self.assertEqual(response.status_code, 200)
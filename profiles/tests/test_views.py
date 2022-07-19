from profiles.tests import factories
from django.urls import reverse
from django.test import TestCase
from profiles.views import profile


class ProfilesTest(TestCase):
    def test_index_view(self):

        user1 = factories.UserFactory(username='test_user_1')
        user2 = factories.UserFactory(username='test_user_2')

        factories.ProfileFactory(user=user1)
        factories.ProfileFactory(user=user2)
        url = ('profiles:index')
        response = self.client.get(url)
        assert response.status_code, 200
         
    def test_view_title(self):
        """Check if the title is OK"""
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, "profile")

        # self.assertEqual(response.status_code, 200)
        # self.assertIn( user1.username, response.content)
        # self.assertIn( user2.username, response.content)
        
    def test_profile_view(self):
        user = factories.UserFactory(
            username='test_user',
            first_name='test_first_name',
            last_name='test_last_name',
            email='test_email_name',
        )
        factories.ProfileFactory(user=user)
        url = reverse(profile,'profile', args=[user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'profiles/profile.html' )
        
        
        # self.assertEqual(response.status_code, 200)
        # assert response.status_code == 200
        # assert b'test_user' in response.content
        # assert b'test_first_name' in response.content
        # assert b'test_last_name' in response.content
        # assert b'test_email' in response.content
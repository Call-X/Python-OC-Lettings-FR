from django.urls import resolve, reverse
from django.test import TestCase


class TestURL(TestCase):
    def test_index(self):
        assert reverse('profiles:index') == '/profiles/'
        assert resolve('/profiles/').view_name == 'profiles:index'


    def test_profile(self):
        assert (
            reverse('profiles:profile', kwargs={'username': 'test_user'})
            == '/profiles/test_user/'
        )
        assert resolve('/profiles/test/').view_name == 'profiles:profile'
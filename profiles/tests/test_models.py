from profiles.tests import factories
import pytest

pytestmark = pytest.mark.django_db

class TestProfile():
    
    def test_profile(self):
        profile = factories.ProfileFactory(
            user=factories.UserFactory(username='test_user')
        )
        print(profile.user.username)
        assert str(profile) == 'test_user'
        assert True

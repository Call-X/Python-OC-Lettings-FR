from profiles.tests import factories
import pytest

pytestmark = pytest.mark.django_db

class TestProfile():
    
    def test_profile(self):
        profile = factories.ProfileFactory(
            user=factories.UserFactory(username='test')
        )
        # print(user_factory.username)
        assert str(profile) == 'test'
        assert True

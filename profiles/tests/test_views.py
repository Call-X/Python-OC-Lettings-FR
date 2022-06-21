import pytest

from . import factories
from .. import views


pytestmark = pytest.mark.django_db


def test_index_view(rf):

    user1 = factories.UserFactory(username='test_user_1')
    user2 = factories.UserFactory(username='test_user_2')

    factories.ProfileFactory(user=user1)
    factories.ProfileFactory(user=user2)

    response = views.index(rf)

    assert response.status_code == 200
    assert b'test_user_1' in response.content
    assert b'test_user_2' in response.content


def test_profile_view(rf):
    user = factories.UserFactory(
        username='test_user',
        first_name='test_first_name',
        last_name='test_last_name',
        email='test_email_name',
    )
    factories.ProfileFactory(user=user)
    response = views.profile(rf, user.username)

    assert response.status_code == 200
    assert b'test_user' in response.content
    assert b'test_first_name' in response.content
    assert b'test_last_name' in response.content
    assert b'test_email' in response.content
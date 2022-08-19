import pytest
from pytest_factoryboy import register
from profiles.tests.factories import UserFactory, ProfileFactory

register(UserFactory)
register(ProfileFactory)

@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user

from profiles.tests import factories

def test_profile():
    profile = factories.ProfileFactory(
        user=factories.UserFactory(username='test')
    )
    assert str(profile) == 'test'

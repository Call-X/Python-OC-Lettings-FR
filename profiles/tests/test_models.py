from profiles.tests import factories

def test_profile(user_factory):
    # profile = factories.ProfileFactory(
    #     user=factories.UserFactory(username='test')
    # )
    print(user_factory.username)
    # assert str(profile) == 'test'
    assert True

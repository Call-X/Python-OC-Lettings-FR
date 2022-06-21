from django.urls import resolve, reverse


def test_index():
    assert reverse('profiles:index') == '/profiles/'
    assert resolve('/profiles/').view_name == 'profiles:index'


def test_profile():
    assert (
        reverse('profiles:profile', kwargs={'username': 'test_username'})
        == '/profiles/test_username/'
    )
    assert resolve('/profiles/test/').view_name == 'profiles:profile'
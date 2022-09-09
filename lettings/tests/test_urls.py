from django.urls import resolve, reverse

class TestUrls():
    def test_index(self):
        assert reverse('lettings:index') == '/lettings/'
        assert resolve('/lettings/').view_name == 'lettings:index'

    def test_lettings(self):
        assert reverse('lettings:letting', kwargs={'letting_id': 1}) == '/lettings/1/'
        assert resolve('/lettings/1/').view_name == 'lettings:letting'
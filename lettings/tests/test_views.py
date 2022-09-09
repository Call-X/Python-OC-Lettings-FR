import pytest
from lettings.tests import factories
from django.test import TestCase
pytestmark = pytest.mark.django_db


class LettingsTest(TestCase):
    def test_index_view(self):
        address1 = factories.AddressFactory(
        number=100,
        street='test street',
    )
        factories.LettingFactory(title='My House 1', address=address1)
        url = '/lettings/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_letting_view(self):
        address1 = factories.AddressFactory(
        number=100,
        street='test street',
    )
        factories.LettingFactory(title='title test', address=address1)
        url = '/lettings/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
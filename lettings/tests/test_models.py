import pytest
from lettings.tests import factories

pytestmark = pytest.mark.django_db

class TestLettings():
    def test_address(self):
        address = factories.AddressFactory(number=10, street='test')
        assert str(address) == '10 test'

    def test_letting(self):
        letting = factories.LettingFactory(title='test')
        assert str(letting) == 'test'
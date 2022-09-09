import factory
from faker import Faker
from lettings.models import Address, Letting
fake = Faker()


class AddressFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Address
    number = fake.building_number()
    street = fake.street_name()
    city = fake.city()
    state = fake.country_code()
    zip_code = fake.postcode()
    country_iso_code = fake.country_code(representation='alpha-3')


class LettingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Letting
    title = fake.text(max_nb_chars=256)
    address = factory.SubFactory(AddressFactory)
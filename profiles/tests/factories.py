import factory
from faker import Faker
from django.contrib.auth.models import User
from profiles.models import Profile

fake = Faker()
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    username = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()
    
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    favorite_city = fake.city()


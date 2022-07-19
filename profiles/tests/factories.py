
import factory
from faker import Faker

from django.contrib.auth.models import User
from profiles.models import Profile
from factory import sequence
fake = Faker()
class UserFactory(factory.django.DjangoModelFactory):
    username = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()
    
    @sequence
    def username(n):
        max_id = User.objects.latest('id').id
        return f'User-{max_id + 1}'
    class Meta:
        model = User
        django_get_or_create = ['username']
      
      
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    favorite_city = fake.city()

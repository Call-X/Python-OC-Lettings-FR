from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address


admin.site.register(Letting)
admin.site.register(Address)
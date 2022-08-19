from django.urls import path
from lettings.views import letting, index


app_name = "lettings"
urlpatterns = [
    path('', index, name='index'),
    path('<int:letting_id>/', letting, name='letting')
]
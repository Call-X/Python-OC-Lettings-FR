from __future__ import division
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)
    

urlpatterns = [
    path("", TemplateView.as_view(template_name="profiles/base_b.html"), name="home"),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('lettings/', include("lettings.urls")),
    path('sentry_debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

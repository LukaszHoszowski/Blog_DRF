from django.contrib import admin
from django.urls import include, path, re_path

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path('')
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

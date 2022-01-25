from django.urls import include, path, re_path

from config import settings

urlpatterns = [
    path("api-auth/", include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

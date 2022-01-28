from django.contrib import admin
from django.urls import include, path, re_path

from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path('api/v1/', include('posts.urls')), #rest login logout
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), #drf tokens
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls'))) #debug

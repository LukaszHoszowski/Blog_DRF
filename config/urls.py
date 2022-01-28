from django.contrib import admin
from django.urls import include, path, re_path

from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path('api/v1/', include('posts.urls')), #rest login logout
    path('api/v1/users/', include('user.urls')), #rest login logout
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), #drf tokens
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), #REGISTRATION
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls'))) #debug

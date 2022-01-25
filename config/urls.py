from django.contrib import admin
from django.urls import include, path, re_path

import posts
from config import settings
import posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path('api/v1/', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

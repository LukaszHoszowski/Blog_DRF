from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import UserViewSet

app_name = 'users'

router = SimpleRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.ClassUserAPIList.as_view(), name="list"),
#     path('<int:pk>/', views.ClassUserAPIDetail.as_view(), name="_detail"),
# ]

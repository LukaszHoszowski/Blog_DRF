from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import PostsViewSet, CommentViewSet

app_name = 'posts'

router = SimpleRouter()
router.register('posts', PostsViewSet, basename='posts')
router.register('comment', CommentViewSet, basename='comments')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.PostAPIList.as_view(), name="list"),
#     path('<int:pk>/', views.PostAPIDetail.as_view(), name="detail"),
# ]

from django.urls import path
from . import views

app_name = 'Posts'

urlpatterns = [
    path('/', views.PostView.as_view(), name="posts"),
]

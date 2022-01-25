from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostAPIList.as_view(), name="list"),
    path('<int:pk>/', views.PostAPIDetail.as_view(), name="detail"),
]

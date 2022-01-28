from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.ClassUserAPIList.as_view(), name="list"),
    path('<int:pk>/', views.ClassUserAPIDetail.as_view(), name="_detail"),
]

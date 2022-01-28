from django.contrib.auth import get_user_model
from rest_framework import generics

from user.serializers import ClassUserSerializer


class ClassUserAPIList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ClassUserSerializer


class ClassUserAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ClassUserSerializer

from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets


# from user.serializers import ClassUserSerializer
#
#
# class ClassUserAPIList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = ClassUserSerializer
#
#
# class ClassUserAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = ClassUserSerializer
from user.serializers import ClassUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = ClassUserSerializer

from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Post
from .permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnlyAdminDelete
from .serializers import PostSerializer


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyAdminDelete,)

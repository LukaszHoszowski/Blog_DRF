from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostAPIList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

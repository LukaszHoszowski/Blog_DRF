from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, mixins

from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnlyAdminDelete, IsAuthorOrReadOnlyAuthorCanEdit, \
    IsAuthorOrReadOnlyTime, NotPostman
from .serializers import PostSerializer, CommentSerializer


# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthorOrReadOnlyAuthorCanEdit,)
#
#
# class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (NotPostman,)


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = NotPostman


# List - GET ALL
# Retrieve - GET DETAIL
# Create - POST ALL
# Update/Partial Update - PUT / PATCH DETAIL
# Destroy - DELETE DETAIL

class CommentViewSet(mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

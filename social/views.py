from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User

from social.models import Post, Like
from social.serializers import UserSerializer, PostSerializer, LikeSerializer


class UserList(generics.ListAPIView):
    """ Render User list """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """ Render User detail """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
    """ Render Posts list """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Render Post detail """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeList(generics.ListCreateAPIView):
    """ Render Like list """

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

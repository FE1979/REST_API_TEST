from rest_framework import generics, renderers, status, viewsets
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User

from social.models import Post, Like
from social.serializers import UserSerializer, PostSerializer, LikeSerializer
from social.likemixin import LikedMixin


# User list and detail views
class UserList(generics.ListCreateAPIView):
    """ Render User list """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]


class UserDetail(generics.RetrieveAPIView):
    """ Render User detail """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


# Post list and detail views
class PostList(generics.ListCreateAPIView):
    """ Render Posts list """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PostDetail(LikedMixin, viewsets.ModelViewSet):
    """ Render Post detail """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


# Like list and detail views (deprecated)
class LikeList(generics.ListCreateAPIView):
    """ Render Like list """

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Render Like details"""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer



# API_Root
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
#        'likes': reverse('like-list', request=request, format=format)
    })

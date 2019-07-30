from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from social import like_func
from .serializers import UserSerializer


class LikedMixin:
    """ Methods to like post """

    @action(detail=True,methods=['POST'], url_path='like', url_name='like')
    def like(self, request, pk=None):
        """ Likes post """

        obj = self.get_object()
        like_func.add_like(obj, request.user)
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=True,methods=['POST'], url_path='unlike', url_name='unlike')
    def unlike(self, request, pk=None):
        """ Removes like from post """

        obj = self.get_object()
        like_func.remove_like(obj, request.user)
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=True,methods=['GET'], url_path='fans', url_name='fans')
    def fans(self, request, pk=None):
        """ Gets users liked post """

        obj = self.get_object()
        users_list = like_func.get_liked_users(obj)
        serializer = UserSerializer(users_list, context={'request': request}, many=True)
        return Response(serializer.data)


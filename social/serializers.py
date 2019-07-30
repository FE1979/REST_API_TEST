from rest_framework import serializers
from django.contrib.auth.models import User
from social.models import Post, Like
import likes_func

class PostSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Posts """

    owner = serializers.ReadOnlyField(source='owner.username')
    likes = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='like-detail',
                                                read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['url', 'id', 'owner', 'is_liked', 'total_likes',
                  'title', 'body', 'created']

    def get_is_liked(self, obj):
        """ Checks if user liked post """

        user = self.context.get('request').user
        return likes_func.is_liked(obj, user)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Likes """

    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='post-detail',
                                                read_only=True)

    class Meta:
        model = Like
        fields = ['url', 'id', 'owner', 'posts']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ User serializer """

    posts = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='post-detail',
                                                read_only=True)
    likes = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='like-detail',
                                                read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts', 'likes']

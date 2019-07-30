from rest_framework import serializers
from django.contrib.auth.models import User
from social.models import Post, Like

class PostSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Posts """

    owner = serializers.ReadOnlyField(source='owner.username')
    likes = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='likes',
                                                read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'id', 'owner', 'likes', 'title', 'body', 'created']

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Likes """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['url', 'id', 'owner', 'post']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ User serializer """

    posts = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='posts',
                                                read_only=True)
    likes = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='likes',
                                                read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts', 'likes']

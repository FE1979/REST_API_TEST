from rest_framework import serializers
from django.contrib.auth.models import User
from social.models import Post, Like
from social.like_func import is_liked

class PostSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Posts """

    liked = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['url', 'id', 'liked', 'total_likes',
                  'title', 'body', 'user', 'created']

    def get_liked(self, obj):
        """ Checks if user liked post """

        user = self.context.get('request').user
        return is_liked(obj, user)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Likes """

    user = serializers.ReadOnlyField(source='user.username')
    posts = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='post-detail',
                                                read_only=True)

    class Meta:
        model = Like
        fields = ['url', 'id', 'user', 'posts']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ User serializer """

    posts = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='post-detail',
                                                read_only=True)
    likes = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='like-detail',
                                                read_only=True)

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'posts', 'likes']

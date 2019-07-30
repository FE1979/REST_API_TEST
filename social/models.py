from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    """ Like for Post """

    user = models.ForeignKey('auth.user', related_name='likes',
                              on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    """ Post created by API user """

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    body = models.TextField()
    user = models.ForeignKey('auth.user', related_name='posts',
                              on_delete=models.CASCADE)
    # link with Like
    likes = GenericRelation(Like)

    # str represent
    def __str__(self):
        return self.body

    # returns number of likes
    @property
    def total_likes(self):
        return self.likes.count()

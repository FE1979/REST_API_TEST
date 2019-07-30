from django.db import models


class Post(models.Model):
    """ Post created by API user """

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    body = models.TextField()
    owner = models.ForeignKey('auth.user', related_name='posts',
                              on_delete=models.CASCADE)

class Like(models.Model):
    """ Like for Post
        Only owner can modify like
        Like is related to the Post
    """

    owner = models.ForeignKey('auth.user', related_name='likes',
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)

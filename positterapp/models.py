from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    positive_score = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    like_num = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(User,
                                verbose_name='user',
                                on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                                verbose_name='posieet',
                                on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class Reply(models.Model):
    reply_id = models.ForeignKey(Post,
                                 verbose_name='id',
                                 on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,
                                verbose_name='id',
                                on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return str(self.id)


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
    display_name = models.CharField(max_length=20)
    birthday = models.DateField(auto_now=False, null=True, blank=True)


class Follow(models.Model):
    user = models.ForeignKey(User,
                        verbose_name='user',
                        on_delete=models.CASCADE)
    
    follow_id = models.CharField(max_length=30)

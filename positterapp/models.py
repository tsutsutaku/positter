from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    positive_score = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user_id = models.ForeignKey(User,
                                verbose_name='id',
                                on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,
                                verbose_name='id',
                                on_delete=models.CASCADE)

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
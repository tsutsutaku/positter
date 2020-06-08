from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    positive_score = models.IntegerField()



class Likes(models.Model):
    user_id = models.ForeignKey(User, verbose_name='id', on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, verbose_name='id', on_delete=models.CASCADE)


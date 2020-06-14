from django.contrib import admin
from .models import Post, Like, Profile, Follow

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Follow)
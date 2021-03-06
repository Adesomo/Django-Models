from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

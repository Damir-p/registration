from django.db import models
from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
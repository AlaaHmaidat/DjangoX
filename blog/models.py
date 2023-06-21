from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

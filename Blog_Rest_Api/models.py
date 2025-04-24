from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    post_image = models.ImageField(upload_to='post_images')

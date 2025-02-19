from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='default.jpg')
    bio = models.TextField(blank=True)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username

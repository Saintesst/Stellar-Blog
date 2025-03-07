from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с пользователем
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Аватар
    bio = models.TextField(blank=True, null=True)  # Биография

    def __str__(self):
        return self.user.username
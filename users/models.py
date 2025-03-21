import os
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Связь с пользователем
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Аватар
    bio = models.TextField(blank=True, null=True)  # Биография

    def __str__(self):
        return self.user.username

def default_avatar():
    """
    Возвращает путь к аватару по умолчанию.
    """
    return os.path.join(settings.MEDIA_URL, 'avatars/default.jpg')

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default=default_avatar, blank=True, null=True)

    # Указываем уникальные related_name для groups и user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",  # Уникальный related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",  # Уникальный related_name
        related_query_name="user",
    )
    

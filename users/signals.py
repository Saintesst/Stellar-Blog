from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import User, Profile
import os

@receiver(post_save, sender=User)
def set_default_avatar(sender, instance, created, **kwargs):
    """
    Устанавливает аватар по умолчанию при создании пользователя.
    """
    if created:  # Проверяем, что пользователь только что создан
        default_avatar_path = os.path.join(settings.MEDIA_URL, 'avatars/default.jpg')
        if not instance.avatar:  # Если аватар не установлен
            instance.avatar = default_avatar_path
            instance.save()
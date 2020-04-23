from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    if settings.AUTH_WITH_EMAIL:
        REQUIRED_FIELDS = []
        objects = CustomUserManager()
        USERNAME_FIELD = 'email'
        email = models.EmailField(max_length=254, unique=True)
    else:
        pass

User = get_user_model()


class UserRecoveryCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField(verbose_name='Codigo')
    created_at = models.DateTimeField(auto_now_add=True)

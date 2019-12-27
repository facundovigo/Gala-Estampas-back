from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .managers import CustomUserManager

class CustomUser(AbstractUser):
	if settings.AUTH_WITH_EMAIL:
		REQUIRED_FIELDS = []
		objects = CustomUserManager()
		USERNAME_FIELD = 'email'
		email = models.EmailField(max_length=254, unique=True)
	else:
		pass

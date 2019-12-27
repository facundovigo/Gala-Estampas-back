from django.contrib.auth.models import AbstractUser
from django.db import models
from baseproject.settings import AUTH_WITH_EMAIL
from .managers import CustomUserManager

class CustomUser(AbstractUser):
	if AUTH_WITH_EMAIL:
		REQUIRED_FIELDS = []
		objects = CustomUserManager()
		USERNAME_FIELD = 'email'
		email = models.EmailField(max_length=254, unique=True)
	else:
		pass
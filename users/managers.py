from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = get_user_model()(email=email)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password=None):
        user = get_user_model()(email=email)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
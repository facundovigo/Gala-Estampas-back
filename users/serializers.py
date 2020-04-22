from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class LoginSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Token
        fields = ('key', 'user')

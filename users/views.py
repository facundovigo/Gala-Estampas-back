from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import LoginSerializer
from .models import User

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = AuthTokenSerializer(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)[0]
        return Response(LoginSerializer(token).data)


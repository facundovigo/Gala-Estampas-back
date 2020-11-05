from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import LoginSerializer, RecoverPasswordSerializer, ChangePasswordSerializer, UserSerializer
from .models import User, UserRecoveryCode

class CustomUserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User(
            username=serializer.validated_data['email'],
            **serializer.validated_data
        )
        user.set_password(serializer.validated_data['password'])
        user.save()

        token = Token.objects.get_or_create(user=user)[0]
        return Response(LoginSerializer(token).data)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = AuthTokenSerializer(data=request.data,
                                           context={'request': request})
        print(request, "req")
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)[0]
        return Response(LoginSerializer(token).data)

    @action(detail=False, methods=['post'])
    def recover_password(self, request):
        serializer = RecoverPasswordSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        import random

        number = random.randrange(10000, 99999)
        usr = get_object_or_404(User, email=request.data['email'])

        UserRecoveryCode.objects.filter(user=usr).delete()

        user_code = UserRecoveryCode.objects.create(user=usr, code=number)

        send_mail(
            'Recupera tu contraseña',
            f'Código de verificación {number}',
            settings.ADMIN_EMAIL,
            [usr.email],
            fail_silently=False,
        )

        #borramos el token anterior, ya que se solicito una recuperacion de contraseña
        Token.objects.filter(user=usr).delete()
        return Response({'sent': True})


    @action(detail=False, methods=['post'])
    def check_code(self, request):
        #Verificamos que exista un codigo asociado a ese email
        user_recovery_code = get_object_or_404(UserRecoveryCode, user__email=request.data['email'],
                                               code=request.data['code'])

        #Verificamos que no esté vencido: la setting PASSWORD_RECOVER_CODE_EXPIRATION nos permite setear en minutos
        #cuanto dura un codigo. Despues de eso está vencido.
        if user_recovery_code.created_at < (timezone.now() - timedelta(**settings.PASSWORD_RECOVER_CODE_EXPIRATION)):
            return Response({'error': 'code expired'}, status=status.HTTP_403_FORBIDDEN)

        #obtenemos un nuevo token
        token = Token.objects.get_or_create(user=user_recovery_code.user)[0]
        return Response(LoginSerializer(token).data)


    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request):
        user = request.user

        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not user.check_password(serializer.validated_data['old_password']):
            return Response({ "error": "INCORRECT_OLD_PASSWORD" }, status=status.HTTP_403_FORBIDDEN)

        user.set_password(serializer.validated_data['new_password'])    
        user.save()

        Token.objects.filter(user=user).delete()
        token = Token.objects.get_or_create(user=user)[0]

        return Response(LoginSerializer(token).data)

    @action(methods=['post'], detail=False, permission_classes=[permissions.IsAuthenticated])
    def set_password(self, request):
        usr = request.user
        usr.set_password(request.data['new_password'])
        usr.save()

        token = Token.objects.get_or_create(user=usr)[0]

        return Response(LoginSerializer(token).data)
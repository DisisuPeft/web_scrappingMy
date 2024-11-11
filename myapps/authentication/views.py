from contextvars import Token

from myapps.authentication.manager import CustomUserManager
from myapps.authentication.models import UserCustomize as User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from myapps.authentication.serializers import UserCustomizeSerializer
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    # data = request.GET.dict()
    serializer = UserCustomizeSerializer(data=request.data)
    # print(request.data)
    if serializer.is_valid():
        user = serializer.save()
        # print(user)
        # Token.objects.create(user=user)
        refresh = RefreshToken.for_user(user)
        # access_token = str(refresh.access_token)
        return Response({'message': 'registrado con exito'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Devuelve los errores de validación
    # Verifica que tanto el email como el password estén presentes
    # if not data.get('email') or not data.get('password'):
    #     return JsonResponse({'error': 'Se deben ingresar tanto el email como el password'}, status=400)
    #
    # Crea el usuario
    # user = User.objects.create_user(email=data['email'], password=data['password'])
    #
    # if not user:
    #     return JsonResponse({'error': 'No se pudo crear el usuario'}, status=400)
    #
    # # Crea el token
    # token = Token.objects.create(user=user)
    # if not token:
    #     return JsonResponse({'error': 'No se pudo crear el token'}, status=400)
    #
    # return JsonResponse({'message': 'Usuario creado con éxito'}, status=200)
    # data = request.GET.dict()
    # print(request.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data['email']

    password = request.data['password']

    if email is None or password is None:
        return Response({"message": "Por favor, proporciona un email y una contraseña."},
                        status=status.HTTP_400_BAD_REQUEST)

    if not User.objects.filter(email=email).exists():
        return Response({"message": "Usuario no encontrado."},
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.get(email=email)

    if not user.check_password(request.data['password']):
        return Response({"message": "La contraseña es incorrecta."},
                        status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)

    s = UserCustomizeSerializer(user)
    # print(token)
    return Response({'refresh': str(refresh), 'access': str(refresh.access_token), "user": s.data}, status=status.HTTP_200_OK)
    # return Response({"token": email, "user": password}, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password

# Registro de usuario
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        password = make_password(request.data['password'])
        email = request.data['email']

        user = User.objects.create(username=username, password=password, email=email)
        return Response({"message": "User created successfully"})

# Login de usuario
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        # Verifica si el usuario existe
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Invalid credentials')

        # Genera o recupera el token
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })

# Verificación de token
class TestTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': f'Hello, {request.user.username}',
        })


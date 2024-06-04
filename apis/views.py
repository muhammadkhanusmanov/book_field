from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db.models import F
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login
from django.middleware.csrf import get_token
from django.contrib.sessions.middleware import SessionMiddleware

class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({'status': False, 'detail': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        token,created = Token.objects.get_or_create(user=user)
        response = Response({'status': True,'token':token}, status=status.HTTP_201_CREATED)
        return response

class LoginUser(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        token,created = Token.objects.get_or_create(user=user)
        return Response({'status':True, 'token':token}) 



class CustomAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    def get(self, request):
        user = request.user
        username = user.username
        return Response({"username": username})
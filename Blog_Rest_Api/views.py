from django.shortcuts import render
from .serializers import ProfileSerializer, PostSerializer, LoginSerializer
from rest_framework.response  import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import PostModel
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'registration succesfull'}, status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
    

class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        print("USER and Password:", username, password)
        if username is None and password is None:
            return Response({'error':'Please provide username & password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials'},
                            status=status.HTTP_404_NOT_FOUND)
     

        refresh = RefreshToken.for_user(user)
        return Response({
                'User Detail':'Succesfully Login',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        


class PostView(ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return PostModel.objects.filter(user=self.request.user)






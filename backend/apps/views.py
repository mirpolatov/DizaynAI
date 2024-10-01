from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import ProductSite, ProductLogo, Register
from apps.serializers import SiteSerializer, LogoSerializer, RegisterSerializer, ProfileSerializer


class SiteModelView(ModelViewSet):
    queryset = ProductSite.objects.all()
    serializer_class = SiteSerializer
    parser_classes = (MultiPartParser,)
    permissions = (IsAuthenticated,)
    http_method_names = ('post', 'get', 'put', 'delete')


class LogoModelView(ModelViewSet):
    queryset = ProductLogo.objects.all()
    serializer_class = LogoSerializer
    parser_classes = (MultiPartParser,)
    permissions = (IsAuthenticated,)
    http_method_names = ('post', 'get', 'put', 'delete')


class RegisterView(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser,)
    http_method_names = ('post', 'get', 'put', 'delete')


class ProfileModelView(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser,)
    permissions = (IsAuthenticated,)
    http_method_names = ('get', 'put', 'delete')


from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

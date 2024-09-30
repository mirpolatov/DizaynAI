from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.models import Register, ProductSite, ProductLogo


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = (
            'image', 'name', 'last_name', 'email', 'phone_number', 'country', 'address', 'password', 'reaped_password')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = (
            'image', 'name', 'last_name', 'company_name', 'email', 'phone_number', 'country', 'address', 'zip_code')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Register.EMAIL_FIELD  # Bu yerda 'email' dan foydalaniladi

    def validate(self, attrs):
        # 'email' ni 'username' o'rniga tekshirish uchun
        self.user = Register.objects.filter(email=attrs['email']).first()
        if self.user is None:
            raise serializers.ValidationError("Invalid email or password")
        return super().validate(attrs)


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSite
        fields = '__all__'


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLogo

        fields = '__all__'

from django.db import models
from django.contrib.auth.models import (
    AbstractUser, User)


class Register(AbstractUser):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    reaped_password = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='register_groups',  # Add a custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='register_user_permissions',  # Add a custom related name
        blank=True
    )

    def __str__(self):
        return self.email


class ProductSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    site_type = models.CharField(max_length=255)
    site_color = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name


class ProductLogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    logo_type = models.CharField(max_length=255)
    logo_color = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

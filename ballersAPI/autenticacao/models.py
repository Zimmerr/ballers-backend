from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email não foi fornecido")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('ativo', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('ativo') is not True:
            raise ValueError("Superuser deve ser ativo")
        if kwargs.get('is_staff') is not True:
            raise ValueError("Superuser deve ser da staff")
        if kwargs.get('is_superuser') is not True:
            raise ValueError("Superuser should have is_superuser=True")
        return self.create_user(email, password, **kwargs)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome']

    objects = UsuarioManager()

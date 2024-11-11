from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from myapps.authentication.manager import CustomUserManager
# from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserCustomize(AbstractUser):
    # username = models.CharField(max_length=50, unique=True)
    username = None
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=50)
    perfilId = models.IntegerField(null=True, default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name='usercustomize_set',  # Cambiamos el related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usercustomize_set',  # Cambiamos el related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.email
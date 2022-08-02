import email
from email.policy import default
from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255 )
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=11, unique=True)
    profile_image = models.ImageField(upload_to ='profile/' , blank = True , null = True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email' ,'full_name']

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

        
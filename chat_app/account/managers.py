from unicodedata import normalize
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number ,email, full_name, password=None):
        if not full_name:
            raise ValueError('Users must have an full_name')
        
        if not phone_number:
            raise ValueError('Users must have an phone number')
        
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            phone_number = phone_number ,
            full_name=full_name ,
            email = self.normalize_email(email)
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number ,email , full_name, password=None):
        user = self.create_user(
            phone_number,
            email,
            full_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
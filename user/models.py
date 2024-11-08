from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email='admin@admin.com'):   # key value kurinishida berilgan parametrlar oxirida yoziladi func da
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):                             #  PermissionsMixin adminga kirishga dostup beradi
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    photo = models.ImageField(upload_to='user/', null=True, blank=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_superuser

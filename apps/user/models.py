from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, firstName, lastName, phone, userStatus, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            username=username,
            lastName=lastName,
            phone=phone,
            userStatus=userStatus
        )

        if not email:
            raise ValueError('Users must have an email address')
        if not firstName:
            raise ValueError('Users must have an firstname')
        if not lastName:
            raise ValueError('Users must have an lastname')
        if not password:
            raise ValueError('Users must have a password')

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname, roles, password=None):
        """
         Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, firstname, lastname, roles, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(('username'), max_length=30, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    userStatus = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'username', 'phone', 'email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, user_name, role, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, role, password, **other_fields)

    def create_user(self, email, user_name, role, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          role=role, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    role = models.CharField(
        choices=(('teacher', 'teacher'), ('student', 'student'), ('admin', 'admin'),), max_length=150, default='student')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=120,null=True)
    last_name = models.CharField(max_length=120,null=True)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateTimeField(default=timezone.now)
    gender = models.CharField(choices=(
        ('male', 'male'), ('female', 'female'), ('transgender', 'transgender'),), max_length=20,default='male')
    standard = models.IntegerField(default=0)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'role', ]

    def __str__(self):
        return self.user_name

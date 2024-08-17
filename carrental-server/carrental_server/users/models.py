from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomAccountManager(BaseUserManager):
    """Custom model to create new users"""

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        """
        Creates superuser
        Sets is_staff, is_superuser and is_active to True and calls create_user()
        to create a superuser.

        Mandatory fields: email and password
        Returns a user object
        """

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, last_name, license_number="admin",
                                date_of_birth=timezone.now(), password=password, **other_fields)

    def create_user(self, email, first_name, last_name, license_number,
                    date_of_birth, password, **other_fields):
        """
        Creates normal user

        Mandatory fields: email, password, first_name and last_name
        Optional fields: middle_name, license_number, date_of_birth, phone_number,
                     address
        Default field: is_staff=False and is_active=True

        Returns user object
        """

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,
                          first_name=first_name, last_name=last_name, license_number=license_number,
                          date_of_birth=date_of_birth, **other_fields)
        user.set_password(password)
        user.save()
        print("saving user")
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    """
    New user class. Email and password will be used to login.
    Mandatory fields: email, first_name and last_name
    Optional fields: middle_name, license_number, date_of_birth, phone_number,
                     address
    Default field: is_staff=False and is_active=True
    """

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=False)
    license_number = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(default="1900-01-01")
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


#drop table if EXISTS auth_permission, users_newuser, users_newuser_user_permissions, auth_group_permissions, django_admin_log, django_content_type, django_migrations, django_session, token_blacklist_outstandingtoken, token_blacklist_blacklistedtoken, users_newuser_groups, auth_group CASCADE

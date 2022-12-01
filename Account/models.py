from django.contrib.auth.models import(AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):
    pass


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, unique=True)
    bio = models.TextField(_('about'), max_length=500, blank=True)
    country = CountryField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['user_name']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    # def email_user(self, subject, message):
    #     send_mail(
    #         subject,
    #         message,
    #         '1@1.com',
    #         [self.email],
    #         fail_silently=False
    #     )

    def __str__(self):
        return self.user_name


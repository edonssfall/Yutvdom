from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(AbstractBaseUser):
    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)
    phone_number = models.CharField(_("Phone number"), max_length=12, unique=True)
    email = models.CharField(_("e-mail"), max_length=255, unique=True)
    password = models.CharField(_("Password"), max_length=255)

    is_admin = models.BooleanField(_("Is Admin"), default=False)

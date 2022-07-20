from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    first_name = models.CharField(_("First Name"), max_length=150)
    last_name = models.CharField(_("Last Name"), max_length=150)
    email = models.CharField(_("E-mail"), max_length=255)
    phone = models.CharField(_("Phone number"), max_length=13)
    password = models.CharField(_("Password"), max_length=150)

    is_admin = models.BooleanField(_("Admin"), default=False)

    def __str__(self):
        return self.email

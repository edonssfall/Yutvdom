from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
#from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=255, blank=True, null=False, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    phone = models.CharField(_("phone number"), max_length=13, blank=True, null=True, unique=True)
    city = models.CharField(_('city'), max_length=255, blank=True, null=True)
    adress = models.CharField(_('adress'), max_length=255, blank=True, null=True)
    zip_code = models.CharField(_('zip code'), max_length=255, null=True)
    is_verified = models.BooleanField(_("verified"), default=False)

    objects = UserManager()

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['phone', 'email']

    class Meta:
        verbose_name = _('user')
        #verbose_name_plurar = _('user')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

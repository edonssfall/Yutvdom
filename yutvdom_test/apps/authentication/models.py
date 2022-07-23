from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, phone, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email and not phone:
            raise ValueError(_('The Email an Phone number must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    phone = PhoneNumberField(_("phone number"), blank=True, null=True, unique=True)
    city = models.CharField(_('city'), max_length=255, blank=True, null=True)
    adress = models.CharField(_('adress'), max_length=255, blank=True, null=True)
    zip_code = models.CharField(_('zip code'), max_length=255, null=True)

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

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

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
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, phone, password, **kwargs):
        user = self.model
        if not username:
            if not email or not phone:
                raise ValueError(_("Enter e-mail or password"))
        if email:
            email = self.normalize_email(email)
            if not username:
                username = email
            user = self.model(
                username=username,
                email=email,
                **kwargs
            )
        if phone:
            if not username:
                username = phone
            user = self.model(
                username=username,
                phone=phone,
                **kwargs
            )
        if kwargs.get('is_superuser'):
            user = self.model(
                username=username,
                **kwargs
            )
        user.set_password(password)
        user.save(usig=self._db)
        return user

    def create_user(self, username, email, phone, password, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(username, email, phone, password, **kwargs)

    def create_superuser(self, username, email, phone, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Super User must be True'))
        return self._create_user(username, email, phone, password, **kwargs)

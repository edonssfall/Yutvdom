from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class AuthenticationBackend(ModelBackend):
    supports_object_permission = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None:
            phone = kwargs.get('phone')
            if phone is None:
                return None
            else:
                try:
                    user = User.objects.get(phone=phone)
                except User.DoesNotExist:
                    return None
        else:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return None
        if User.check_password(password):
            return user
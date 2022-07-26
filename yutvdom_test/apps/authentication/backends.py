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

    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(email=email) | Q(email=phone)
            )
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        else:
            return None


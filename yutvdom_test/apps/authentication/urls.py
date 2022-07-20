from django.urls import path
from .views import sign_up

app_name = 'apps.authentication'

urlpatterns = [
    path("", sign_up)
]

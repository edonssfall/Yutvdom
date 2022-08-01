from django.urls import path
from .views import RegisterView, LoginView, LogoutView, home

app_name = 'apps.authentication'

urlpatterns = [
    path('', home, name='home'),
    path("authentication/sign_up", RegisterView.as_view(), name='register-user'),
    path('authentication/sign_in', LoginView.as_view(), name='login-user'),
    path('authentication/logout', LogoutView.as_view(), name='logout-user'),
    path('authentication/profile', LogoutView.as_view(), name='profile')
]

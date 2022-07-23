from django.urls import reverse
from django.contrib.auth import login, logout, get_user_model
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import User
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import FormView
from django.shortcuts import render

User = get_user_model()


def home(request):
    return render(request, 'base.html')


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'authentication/sign_in.html'

    def form_valid(self, form):
        login(self.request, User.objects.get(email=form.cleaned_data['email']))
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'authentication/sign_up.html'
    success_url = '/'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,
                             "User successfully registered"
                             "We've sent you an email to confirm your email")
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:user-login'))

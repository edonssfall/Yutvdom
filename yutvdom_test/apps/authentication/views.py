from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, get_user_model
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.views import View
from django.views.generic import FormView
from django.shortcuts import render

User = get_user_model()


def home(request):
    return render(request, 'base.html')


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'authentication/sign_in.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, User.objects.get(email=form.cleaned_data['email']))
        return super().form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'authentication/sign_up.html'
    success_url = 'sign_in'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             "User successfully registered! "
                             "We've sent you an email to confirm your email")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('authentication:login-user'))
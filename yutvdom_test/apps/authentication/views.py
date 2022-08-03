from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, get_user_model
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.views import View
from django.views.generic import FormView
from django.shortcuts import render
import time

User = get_user_model()


def home(request):
    now_time = time.strftime("%c")
    return render(request, 'home.html', context={'now_time': now_time})


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        login(
            self.request,
            User.objects.get(email=form.cleaned_data['email']),
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = '/'

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
        return HttpResponseRedirect(reverse('authentication:home'))
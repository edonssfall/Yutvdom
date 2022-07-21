from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.http import HttpResponse


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(nickname=cd['nickname'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("OK")
                else:
                    return HttpResponse("Denied")
            else:
                return HttpResponse("Invalid login")
        else:
            form = LoginForm()
            return render(request, 'authentication.sign_in.html', {'form': form})

from .forms import LoginForm, RegisterForm


def get_context_data(request):
    context = {
        'login_modal': LoginForm(),
        'register_modal': RegisterForm()
    }
    return context
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    nickname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_user(self):
        email = self.cleaned_data('email', '')
        password = self.cleaned_data('password', '')
        user = User.objects.filter(email=email).first()

        if not user.check_password(password) or user:
            raise forms.ValidationError(_("Incorrect email or password"))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']

    password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_("Repeat Password"))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(_("Password doesn't match"))

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            user.set_password(self.cleaned_data['password'])
        return user

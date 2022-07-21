from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class LoginForm(forms):
    nickname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class Register(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (_('Phone number'), _('e-mail'))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(_("Password doesn't match"))
        return cd['password2']

from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password(self):
        email = self.cleaned_data.get('email', '')
        password = self.cleaned_data.get('password', '')
        user = User.objects.filter(email=email).first()

        if not user:
            raise forms.ValidationError(_("Incorrect email or password"))

        if not user.check_password(password):
            raise forms.ValidationError(_("Incorrect email or password"))
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label=_("Repeat Password"))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(_("Password doesn't match"))

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            user.set_password(self.cleaned_data['password1'])
            user.save()
        return user

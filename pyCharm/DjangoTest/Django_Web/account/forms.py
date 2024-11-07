from django import forms
from django.contrib.auth.hashers import check_password
from .models import account

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address.'
        },
        max_length=64, label='E-Mail'
    )
    password = forms.CharField(
        error_messages={
            'required': 'Please enter your password'
        },
        widget=forms.PasswordInput, label='Password'
    )
    re_password = forms.CharField(
        error_messages={
            'required': 'Please enter your password'
        },
        widget=forms.PasswordInput, label='Password check'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'They have different passwords.')
                self.add_error('re_password', 'They have different passwords.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address.'
        },
        max_length=64, label='E-Mail'
    )
    password = forms.CharField(
        error_messages={
            'required': 'Please enter your password'
        },
        widget=forms.PasswordInput, label='Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                Account = account.objects.get(email=email)
            except account.DoesNotExist:
                self.add_error('email', "don't have an email.")
                return

            if not check_password(password, Account.password):
                self.add_error('password', 'Wrong password')

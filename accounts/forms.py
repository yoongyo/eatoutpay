from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'id': 'username',
            'type': 'text',
            'class': 'mt-4 mb-2',
            'value': "",
            'required autofocus': True,
            'placeholder': 'ID',
            'autocomplete': 'off',
            'style': 'background-color: rgb(225,232,232)'
        }
    ))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'type': 'password',
                'class': 'mt-2 mb-2',
                'placeholder': 'Password',
                'required data-eye': True,
                'autocomplete': 'off',
                'style': ''
            }
        ),
    )
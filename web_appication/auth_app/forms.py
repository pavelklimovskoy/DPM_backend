from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, \
    SetPasswordMixin
from pip._internal.utils._jaraco_text import _

from auth_app.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'input_data', 'placeholder': 'Имя пользователя'}
    ))
    email = forms.EmailField(
        label="",
        max_length=254,
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'input_data', 'placeholder': 'Почта'})
    )
    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input_password', 'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input_password', 'placeholder': 'Подтверждение пароля'})
    )

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'input_data', 'placeholder': 'Имя пользователя'}
    ))
    password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input_password', 'placeholder': 'Пароль'})
    )


class FileUploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(attrs={
            'accept': '.pdf,.docx'
        })
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="",
        max_length=254,
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'input_data', 'placeholder': 'Почта'})
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Новый пароль",
        required=False,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input_password",
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label="Новый пароль",
        required=False,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input_password",
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

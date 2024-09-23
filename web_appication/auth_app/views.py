from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import SignUpForm, LoginForm, FileUploadForm, CustomPasswordResetForm, CustomSetPasswordForm
from django.conf import settings

from .models import UserProfile


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(
                'Приветствуем',
                'Спасибо за регистрацию на Digitalprofessional.me',
                email_from,
                recipient_list,
            )

            recipient_list = ['klimovskoy@sfedu.ru', ]
            send_mail(
                'Приветствуем',
                f'на Digitalprofessional.me зарегистрировался {user.email}',
                email_from,
                recipient_list,
            )

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user.email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']

            user = UserProfile.objects.get(id=request.user.id)
            user.cv_was_uploaded = True
            user.save()

            return redirect('/')
    else:
        form = FileUploadForm()
        form.file.attrs['class'] = 'form-control'
    return render(request, 'file_upload.html', {'form': form})


class NewPasswordView(TemplateView):
    template_name = 'registration/new_password.html'


class ProfileLogoutView(LogoutView):
    http_method_names = ["post", "options", ]
    next_page = '/'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm

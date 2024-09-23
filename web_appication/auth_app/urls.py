from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import NewPasswordView, ProfileLogoutView, file_upload_view, CustomPasswordResetView, \
    CustomPasswordResetConfirmView

urlpatterns = [
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/new_password/', NewPasswordView.as_view(), name='new_password'),
    path('accounts/logout/', ProfileLogoutView.as_view(next_page='/'), name='logout'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('cv-upload/', file_upload_view, name='cv_upload'),
]

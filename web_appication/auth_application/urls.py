from django.urls import path

from .views import *

urlpatterns = [
    path('login-page/', LoginView.as_view()),
]
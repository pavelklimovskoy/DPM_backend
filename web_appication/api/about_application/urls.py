from django.urls import path

from .views import *

urlpatterns = [
    path('', PageView.as_view()),
]

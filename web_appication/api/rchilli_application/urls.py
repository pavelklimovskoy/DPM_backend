from django.urls import path

from .views import *

urlpatterns = [
    path('parse_cv/', CVParseView.as_view()),
]
from django.urls import path

from .views import *

urlpatterns = [
    path('all/', CVView.as_view()),
]

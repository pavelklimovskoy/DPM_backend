from django.urls import path
from .views import *

urlpatterns = [
    path('health/', HealthView.as_view()),
    path('version/', VersionView.as_view()),
]
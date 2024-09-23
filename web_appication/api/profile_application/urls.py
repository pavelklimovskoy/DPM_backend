from django.urls import path
from .views import *

urlpatterns = [
    path('<int:profileId>', ProfileView.as_view()),
    path('<int:profileId>/detail/', ProfileDetailView.as_view()),
    # path('version/', VersionView.as_view()),
]
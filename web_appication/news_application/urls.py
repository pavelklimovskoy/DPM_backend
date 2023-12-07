from django.urls import path

from .views import *

urlpatterns = [
    path('', AllNewsPage.as_view()),
    path('<int:newsId>/', NewsPage.as_view()),
]
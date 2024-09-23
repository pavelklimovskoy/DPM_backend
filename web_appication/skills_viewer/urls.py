from django.urls import path

from .views import SkillsViewer

urlpatterns = [
    path('', SkillsViewer.as_view(), name='skill_viewer'),
]

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from auth_app.models import UserProfile


class SkillsViewer(LoginRequiredMixin, View):

    def get(self, request):

        user_id = request.user.id
        if not UserProfile.objects.get(id=user_id).cv_was_uploaded:
            return render(request, "first_cv_upload.html", context={})

        return render(request, "common_profile.html", context={})

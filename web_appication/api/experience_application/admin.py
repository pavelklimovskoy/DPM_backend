from django.contrib import admin
from .models import *


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    """

    """
    pass


@admin.register(JobProfile)
class JobProfileAdmin(admin.ModelAdmin):
    """

    """
    pass


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    """

    """
    pass


@admin.register(ExperienceModel)
class ExperienceAdmin(admin.ModelAdmin):
    """

    """
    pass

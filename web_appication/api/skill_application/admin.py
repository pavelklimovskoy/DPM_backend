from django.contrib import admin
from .models import *


@admin.register(SegregatedSkillModel)
class SegregatedSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillInfoModel)
class SkillInfoAdmin(admin.ModelAdmin):
    pass

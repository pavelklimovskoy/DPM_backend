from django.contrib import admin
from .models import *


@admin.register(PersonalInfoModel)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(NameModel)
class NameAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageModel)
class LanguageAdmin(admin.ModelAdmin):
    pass

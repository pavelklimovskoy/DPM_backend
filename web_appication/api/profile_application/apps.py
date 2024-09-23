from django.apps import AppConfig


class ProfileApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.profile_application'
    verbose_name = "Профили пользователей"

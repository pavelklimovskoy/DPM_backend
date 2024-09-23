from django.apps import AppConfig


class AuthApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.auth_application'
    verbose_name = "Авторизация пользователей"

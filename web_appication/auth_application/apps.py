from django.apps import AppConfig


class AuthApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_application'
    verbose_name = "Авторизация пользователей"

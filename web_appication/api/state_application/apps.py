from django.apps import AppConfig


class StateApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.state_application'
    verbose_name = "Состояние сайта"

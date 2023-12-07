from django.apps import AppConfig


class NewsApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_application'
    verbose_name = "Новости и анонсы"

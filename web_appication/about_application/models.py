from django.db import models

from tinymce import models as tinymce_models


class AboutPageModel(models.Model):
    """
    Модель для хранения контента для страницы About
    """

    content_ru = tinymce_models.HTMLField(
        default=""
    )
    content_en = tinymce_models.HTMLField(
        default=""
    )

    class Meta:
        verbose_name = 'Контент страницы'
        verbose_name_plural = 'Контент страницы'

    def __str__(self):
        return "Контент страницы About"

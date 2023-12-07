from django.db import models
from tinymce import models as tinymce_models


class NewsPost(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="Заголовок новости"
    )
    title_image = models.FileField(
        verbose_name="Картинка заголовка новости",
        blank=True,
        default=True
    )

    date_creation = models.DateTimeField(
        verbose_name="Дата создания новости"
    )
    is_published = models.BooleanField(default=False)

    body = tinymce_models.HTMLField(
        default=""
    )

    views_count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ("-date_creation",)
    #
    # def get_absolute_url(self):
    #     return "url"

    def __str__(self):
        return f'id={self.id} title={self.title} date={self.date_creation}'

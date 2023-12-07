from django.db import models


class Employee(models.Model):
    """
    Модель для описания сотрудника на странице About
    """
    avatar = models.FileField(
        verbose_name="Аватарка",
        blank=True
    )

    fullname_ru = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    fullname_en = models.CharField(max_length=100)

    position_ru = models.CharField(
        max_length=200,
        verbose_name="Должность"
    )
    position_en = models.CharField(max_length=200)

    is_showed = models.BooleanField(
        default=True,
        verbose_name="Показывать в списке"
    )

    email = models.EmailField(
        null=True,
        blank=True,
        default=""
    )

    show_email = models.BooleanField(
        default=False,
        verbose_name="Отображать почту"
    )

    class Meta:
        ordering = ['id', ]
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    def __str__(self):
        return f'{self.fullname_ru} {self.position_ru} {self.email}'

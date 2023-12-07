from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from cv_application.models import *


class Profile(AbstractUser):
    """
    Расширение модели User из Django
    """

    AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # files = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)
    # files = models.ManyToManyField(File)

    avatar = models.FileField(
        verbose_name="Аватарка",
        blank=True,
        default=None
    )
    langauge = models.CharField(
        null=True,
        blank=True
    )

    uploaded_cv = models.ForeignKey(CVModel,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True
                                    )

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"id={self.id} user_name={self.username}"

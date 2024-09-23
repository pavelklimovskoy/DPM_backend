from datetime import datetime

from django.db import models


# Create your models here.

class State(models.Model):
    is_active = models.BooleanField(default=True)
    launch_time = models.DateTimeField()

    class Meta:
        verbose_name = "Состояние сайта"
        verbose_name_plural = "Состояние сайта"

    # def __init__(self):
    #     self.is_active = True
    #     self.launch_time = datetime.now().strftime("%H:%M:%S")

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    bonus_points = models.IntegerField(blank=True, null=True, default=0)

    cv_was_uploaded = models.BooleanField(default=False)

    cv_file = models.FileField(upload_to='cv_files/', blank=True, null=True, default=None)
    rchilli_data = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.id} {self.username} {self.phone_number}'

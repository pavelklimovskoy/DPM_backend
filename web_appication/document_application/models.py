from django.db import models


class PassportDetailModel(models.Model):
    """
    Модель для описания паспортных данных
    """
    passport_number = models.CharField()
    date_of_expire = models.CharField()
    date_of_issue = models.CharField()
    place_of_issue = models.CharField()


class DocumentInfoModel(models.Model):
    """
    Модель для описания информации о документах пользователя
    """
    unique_id = models.CharField()
    license_no = models.CharField()
    pan_no = models.CharField()
    visa_status = models.CharField()

    passport_detail = models.OneToOneField(PassportDetailModel, on_delete=models.CASCADE)

from api.contact_application.models import *
from api.personal_info_application.models import PersonalInfoModel
from api.skill_application.models import SkillInfoModel
from api.document_application.models import DocumentInfoModel


class FileInfo(models.Model):
    """
    Модель для описания информации о загружаемом файле
    """
    cloud_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    resume_file_name = models.CharField(max_length=256)
    parsing_date = models.DateTimeField(auto_now_add=True, blank=True)


class CVCategory(models.Model):
    """
    Модель для описания категории загружаемого резюме
    """

    category = models.CharField(
        default="default_category"
    )
    sub_category = models.CharField(
        default="default_category"
    )


class CVModel(models.Model):
    """
    Модель для описания резюме пользователя
    """
    file_info = models.OneToOneField(FileInfo, on_delete=models.CASCADE)

    document_info = models.OneToOneField(DocumentInfoModel, on_delete=models.CASCADE)

    cv_category = models.OneToOneField(CVCategory, on_delete=models.DO_NOTHING)
    contact_info = models.OneToOneField(ContactInfo, on_delete=models.CASCADE)

    personal_info = models.OneToOneField(PersonalInfoModel, on_delete=models.CASCADE)

    skill_info = models.OneToOneField(SkillInfoModel, on_delete=models.CASCADE)

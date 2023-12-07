from django.apps import AppConfig


class EmployeeApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee_application'
    verbose_name = "отображаемые сотрудники на странице About"

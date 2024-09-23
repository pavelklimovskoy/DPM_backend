from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from rest_framework.views import APIView

from application_core.settings import DEBUG
from api.employee_application.models import Employee
from api.employee_application.serializers import RuEmployeeSerializers, EnEmployeeSerializers
from .models import AboutPageModel


class PageView(APIView):
    """
    Страница About с информацией о проекте и сотрудниками
    """

    def get(self, request: WSGIRequest) -> render:
        """
        Передача данных в шаблон в зависимости от языка в заголовке запроса
        :param request:
        :return:
        """

        employees = Employee.objects.all()
        page_content = AboutPageModel.objects.last()

        employee_serializer = ""
        response_page_content = ""

        if request.LANGUAGE_CODE == 'ru':
            employee_serializer = RuEmployeeSerializers(employees, many=True)
            response_page_content = page_content.content_ru
        else:
            employee_serializer = EnEmployeeSerializers(employees, many=True)
            response_page_content = page_content.content_en

        return render(request, 'about_application/templates/about_application/index.html',
                      {
                          'debug': DEBUG,
                          'employees': employee_serializer.data,
                          'page_content': response_page_content
                      })

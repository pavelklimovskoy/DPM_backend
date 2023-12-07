from django.core.handlers.wsgi import WSGIRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from typing_extensions import Type

from .serializers import *
from .serializers import RuEmployeeSerializers, EnEmployeeSerializers


class EmployeesView(APIView):
    """
    Получение информации обо всех сотрудниках на двух языках
    """

    def get(self, request: WSGIRequest) -> Response:
        employees = Employee.objects.all()
        serializer = EmployeeSerializers(employees, many=True)

        return Response(serializer.data)


class GetLangEmployeesView(APIView):
    def get_ru_employee(self, request: WSGIRequest) -> Response:
        """
        Получение информации о сотрудниках на русском языке
        :param request:
        :return:
        """
        employees = Employee.objects.all()
        serializer = RuEmployeeSerializers(employees, many=True)

        return Response(serializer.data)

    def get_en_employee(self, request: WSGIRequest) -> Response:
        """
        Получение информации о сотрудниках на английском языке
        :param request:
        :return:
        """
        employees = Employee.objects.all()
        serializer = EnEmployeeSerializers(employees, many=True)

        return Response(serializer.data)

    def get(self, request: WSGIRequest, language: str) -> None:
        """
        Возврат информации о сотрудниках на языке в соответствие с языком запроса
        :param request:
        :param language:
        :return:
        """
        match language:
            case 'ru':
                return self.get_ru_employee(request)
            case 'en':
                return self.get_en_employee(request)
            case _:
                return self.get_en_employee(request)


class GetEmployeeView(APIView):
    def get(self, request: WSGIRequest, employeeId: int) -> Response:
        """
        Получение информации о сотруднике по id
        :param request:
        :param employeeId:
        :return:
        """
        try:
            employee = Employee.objects.get(id=employeeId)
            serializer = EmployeeSerializers(employee, many=False)

            return Response(serializer.data)
        except Employee.DoesNotExist as error:
            return Response({f"Employee with id={employeeId} not found"}, status=404)


class GetEmployeesByLangView(APIView):
    def select_serializer(self, language: str) -> Type[RuEmployeeSerializers] | Type[EnEmployeeSerializers]:
        match language:
            case 'ru':
                return RuEmployeeSerializers
            case 'en':
                return EnEmployeeSerializers
            case _:
                return EnEmployeeSerializers

    def get(self, request: WSGIRequest, employeeId: int, language: str) -> Response:
        """
        Получение информации о сотруднике по id и указанному языку
        :param request:
        :param employeeId:
        :param language:
        :return:
        """
        try:
            employee = Employee.objects.get(id=employeeId)
            serializer = self.select_serializer(language)

            return Response(serializer(employee).data)
        except Employee.DoesNotExist as error:
            return Response({f"Employee with id={employeeId} not found"}, status=404)


class HideEmployeeView(APIView):
    def patch(self, request: WSGIRequest, employeeId: int) -> Response:
        """
        Сокрытие сотрудника из списка по id
        :param request:
        :param employeeId:
        :return:
        """

        try:
            employee = Employee.objects.get(id=employeeId)
            employee.is_showed = False
            employee.save()

            return Response({f"Employee with id={employeeId} hided"}, status=200)
        except Employee.DoesNotExist as error:
            return Response({f"Employee with id={employeeId} not found"}, status=404)


class ShowEmployeeView(APIView):
    def patch(self, request: WSGIRequest, employeeId: int) -> Response:
        """
        Включение отображения сотрудника из списка по id
        :param request:
        :param employeeId:
        :return:
        """

        try:
            employee = Employee.objects.get(id=employeeId)
            employee.is_showed = True
            employee.save()

            return Response({f"Employee with id={employeeId} showed"}, status=200)
        except Employee.DoesNotExist as error:
            return Response({f"Employee with id={employeeId} not found"}, status=404)


class DeleteEmployeeView(APIView):
    def delete(self, request: WSGIRequest, employeeId: int) -> Response:
        """
        Удаление сотрудника по id
        :param request:
        :param employeeId:
        :return:
        """

        try:
            employee = Employee.objects.get(id=employeeId)
            employee.delete()

            return Response({f"Employee with id={employeeId} deleted"}, status=200)
        except Employee.DoesNotExist as error:
            return Response({f"Employee with id={employeeId} not found"}, status=404)

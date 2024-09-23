from django.urls import path

from .views import *

urlpatterns = [
    path('employees/', EmployeesView.as_view()),
    path('employees/<str:language>', GetLangEmployeesView.as_view()),
    path('employee/<int:employeeId>', GetEmployeeView.as_view()),
    path('employee/<int:employeeId>/<str:language>', GetEmployeesByLangView.as_view()),
    path('employee/hide/<int:employeeId>', GetEmployeeView.as_view()),
    path('employee/show/<int:employeeId>', ShowEmployeeView.as_view()),
    path('employee/delete/<int:employeeId>', DeleteEmployeeView.as_view()),
]

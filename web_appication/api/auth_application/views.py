from application_core.settings import DEBUG
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginView(APIView):
    """
    Описание методов для авторизации
    """
    def get(self, request):
        return render(request, 'auth_application/templates/auth_application/auth_login.html', {'debug': DEBUG})

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        print(username, password)

        if user is not None:
            print("logged")
            return Response({"logged"})
        else:
            print("invalid data")
            return Response(status=400)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from application_core.settings import DEBUG


# Create your views here.
class CVParseView(APIView):
    """
    Описание методов обработки резюме
    """

    def get(self, request):
        pass

    def post(self, request):
        pass

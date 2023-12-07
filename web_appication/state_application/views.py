from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from application_core.settings import API_VERSION


# Create your views here.

class HealthView(APIView):
    def get(self, request):
        return Response(status=200)


class VersionView(APIView):
    def get(self, request):
        return Response({'version': API_VERSION})

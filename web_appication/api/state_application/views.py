from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    def get(self, request):
        return Response(status=200)


class VersionView(APIView):
    def get(self, request):
        return Response({'version': settings.API_VERSION})

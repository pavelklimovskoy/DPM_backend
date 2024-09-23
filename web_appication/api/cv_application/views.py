from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import *
from .serializers import *


class CVView(APIView):
    def get(self, request):
        cv = CVModel.objects.all()
        serializer = CVModelSerializer(cv, many=True)

        return Response(serializer.data, status=200)


class CheckViewSet(ViewSet):
    pass

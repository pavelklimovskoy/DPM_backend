from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

from .models import Profile


class ProfileView(APIView):
    def get(self, request: WSGIRequest, profileId: int) -> render:
        try:
            profile = Profile.objects.get(id=profileId)
            return render(request, 'profile.html')
        except Profile.DoesNotExist as error:
            return Response(status=404)


class ProfileDetailView(APIView):
    def get(self, request: WSGIRequest, profileId: int):
        try:
            profile = Profile.objects.get(id=profileId)
            serializer = ProfileSerializer(profile, many=False)
            return Response(serializer.data, status=200)
        except Profile.DoesNotExist as error:
            return Response(status=404)

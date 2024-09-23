from rest_framework import serializers

from .models import State


class StateSerializer(serializers.Serializer):
    class Meta:
        model = State
        fields = '__all__'

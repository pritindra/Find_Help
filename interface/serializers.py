from rest_framework import serializers
from .models import Assistance, CanAssist


class AssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = '__all__'

class CanAssistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanAssist
        fields = '__all__'


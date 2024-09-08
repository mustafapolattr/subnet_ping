from rest_framework import serializers
from ping.models.ping_result import PingResult


class PingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingResult
        fields = '__all__'

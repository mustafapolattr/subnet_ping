from rest_framework import viewsets
from ping.models.ping_result import PingResult
from ping.rest.serializers.ping_result import PingResultSerializer


class PingResultViewSet(viewsets.ModelViewSet):
    queryset = PingResult.objects.all()
    serializer_class = PingResultSerializer

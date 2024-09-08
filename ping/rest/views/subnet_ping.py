from rest_framework.views import APIView
from rest_framework.response import Response
from ping.services.ip_address import IPAddressService
from ping.tasks.ping_ip import ping_ip_task


class SubnetPingView(APIView):

    def post(self, request):
        network = request.data.get('network')
        try:
            ip_list = IPAddressService.get_ip_list(network)
            for ip in ip_list:
                ping_ip_task.delay(ip)
            return Response({"message": "Pinging work queued."})
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
from celery import shared_task
import subprocess
from ping.models.ping_result import PingResult


@shared_task
def ping_ip_task(ip):
    try:
        # "-n" for Windows, "-c" for Linux
        output = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
        is_active = output.returncode == 0

        PingResult.objects.create(ip_address=ip, is_active=is_active)
        return is_active
    except Exception as e:
        PingResult.objects.create(ip_address=ip, is_active=False)
        return False

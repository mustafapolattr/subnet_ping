from django.db import models


class PingResult(models.Model):
    ip_address = models.GenericIPAddressField()
    is_active = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {'Active' if self.is_active else 'Inactive'}"

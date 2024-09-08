from django.contrib import admin
from ping.models.ping_result import PingResult

@admin.register(PingResult)
class PingResultAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'is_active', 'timestamp')

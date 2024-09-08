from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ping.rest.views.ping_result import PingResultViewSet
from ping.rest.views.subnet_ping import SubnetPingView

router = DefaultRouter()
router.register(r'ping-results', PingResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subnet-ping/', SubnetPingView.as_view(), name='subnet-ping'),
]
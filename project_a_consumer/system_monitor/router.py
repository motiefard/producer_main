from rest_framework import routers
from .viewsets import SystemStatusViewSet

# app_name = 'system_monitor'

router = routers.DefaultRouter()
router.register('status', SystemStatusViewSet)
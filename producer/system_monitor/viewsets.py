from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from .models import SystemStatus
from .serializers import SystemStatusSerializer


class SystemStatusPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class SystemStatusViewSet(viewsets.ModelViewSet):
    queryset = SystemStatus.objects.all()
    serializer_class = SystemStatusSerializer
    pagination_class = SystemStatusPagination
    ordering = ['-timestamp']

    def get_queryset(self):
        queryset = SystemStatus.objects.all()
        
        return queryset
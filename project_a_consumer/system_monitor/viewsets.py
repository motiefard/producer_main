from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from .models import SystemStatus
from .serializers import SystemStatusSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view



class SystemStatusPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema_view(
    list=extend_schema(summary="a summary: list system statuses", description="...some description ..."),
    retrieve=extend_schema(exclude=False),  # hide from Swagger
)
class SystemStatusViewSet(viewsets.ModelViewSet):
    queryset = SystemStatus.objects.all()
    serializer_class = SystemStatusSerializer
    pagination_class = SystemStatusPagination
    ordering = ['-timestamp']

    def get_queryset(self):
        queryset = SystemStatus.objects.all()
        
        return queryset
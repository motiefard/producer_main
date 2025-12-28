from rest_framework import serializers
from .models import SystemStatus


class SystemStatusSerializer(serializers.ModelSerializer):
    
    ram_total_gb = serializers.ReadOnlyField()
    disk_total_gb = serializers.ReadOnlyField()
    
    class Meta:
        model = SystemStatus
        fields = [
            'url',
            'id',
            'timestamp',
            'created_at',
            'ram_total',
            'ram_used',
            'ram_free',
            'cpu_percent',
            'disk_total',
            'disk_used',
            'disk_free',
            'raw_data',
            'ram_total_gb',
            'disk_total_gb',
        ]
        read_only_fields = ['id', 'created_at']



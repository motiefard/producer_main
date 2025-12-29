from django.db import models
from django.utils import timezone


class SystemStatus(models.Model):
    """Model to store system status"""
    
    timestamp = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    ram_total = models.BigIntegerField(help_text="Total RAM in bytes")
    ram_used = models.BigIntegerField(help_text="Used RAM in bytes")
    ram_free = models.BigIntegerField(help_text="Free RAM in bytes")
    
    cpu_percent = models.FloatField(help_text="CPU usage percentage")
    
    
    disk_total = models.BigIntegerField(help_text="Total disk space in bytes")
    disk_used = models.BigIntegerField(help_text="Used disk space in bytes")
    disk_free = models.BigIntegerField(help_text="Free disk space in bytes")
    
    
    # Raw JSON data for reference
    raw_data = models.JSONField(default=dict, help_text="Original JSON message from Kafka")
    
    class Meta:
        db_table = 'system_status'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp']),
        ]
    
    def __str__(self):
        return f"System Status at {self.timestamp}"
    
    @property
    def ram_total_gb(self):
        """Return RAM total in GB"""
        return self.ram_total / (1024 ** 3)
    
    @property
    def disk_total_gb(self):
        """Return disk total in GB"""
        return self.disk_total / (1024 ** 3)

# views.py
import psutil
from django.http import JsonResponse

def system_stats_producer(request):
    memory = psutil.virtual_memory()
    ram_info = {
        'ram_total': memory.total,
        'ram_used': memory.used,
        'ram_free': memory.free
    }
    
    cpu_info = {
        'cpu_percent': psutil.cpu_percent(interval=1),
    }
    
    disk = psutil.disk_usage('/')
    disk_info = {
        'disk_total': disk.total,
        'disk_used': disk.used,
        'disk_free': disk.free,
    }
    data = {**ram_info, **cpu_info, **disk_info}
    return data

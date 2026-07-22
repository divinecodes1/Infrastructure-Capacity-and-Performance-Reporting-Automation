import platform
from datetime import datetime


def collect_linux_metrics() -> dict:
    cpu_percent = 72
    memory_percent = 68
    disk_percent = 81
    uptime_seconds = 125000
    service_status = "healthy"

    if cpu_percent > 80 or memory_percent > 80 or disk_percent > 85:
        service_status = "warning"
    if disk_percent > 85:
        service_status = "critical"

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": platform.node() or "demo-host",
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "uptime_seconds": uptime_seconds,
        "service_status": service_status,
    }

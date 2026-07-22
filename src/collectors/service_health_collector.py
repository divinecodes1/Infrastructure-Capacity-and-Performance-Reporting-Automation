def collect_service_health() -> dict:
    return {
        "service": "clearing-service-demo",
        "availability_percent": 99.4,
        "response_time_ms": 210,
        "failed_health_checks": 3,
        "pod_restarts": 1,
        "status": "healthy",
    }

def collect_kubernetes_metrics() -> dict:
    return {
        "pods": [
            {"name": "trading-api-demo", "status": "Running", "restarts": 2},
            {"name": "clearing-service-demo", "status": "Running", "restarts": 1},
        ],
        "node_capacity": {"cpu": 80, "memory": 70, "disk": 60},
        "failed_jobs": 0,
        "deployment_ready": True,
    }

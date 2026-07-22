from src.collectors.service_health_collector import collect_service_health


def test_collect_service_health_returns_expected_shape():
    metrics = collect_service_health()

    assert metrics["availability_percent"] >= 0
    assert metrics["response_time_ms"] >= 0
    assert metrics["failed_health_checks"] >= 0
    assert metrics["status"] in {"healthy", "warning", "critical"}

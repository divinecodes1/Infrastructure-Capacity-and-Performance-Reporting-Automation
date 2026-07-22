from src.collectors.linux_metrics_collector import collect_linux_metrics


def test_collect_linux_metrics_returns_expected_keys():
    metrics = collect_linux_metrics()

    assert metrics["cpu_percent"] >= 0
    assert metrics["memory_percent"] >= 0
    assert metrics["disk_percent"] >= 0
    assert metrics["uptime_seconds"] >= 0
    assert metrics["service_status"] in {"healthy", "warning", "critical"}

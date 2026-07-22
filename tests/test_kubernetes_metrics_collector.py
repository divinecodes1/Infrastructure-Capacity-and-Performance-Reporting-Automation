from src.collectors.kubernetes_metrics_collector import collect_kubernetes_metrics


def test_collect_kubernetes_metrics_returns_expected_shape():
    metrics = collect_kubernetes_metrics()

    assert "pods" in metrics
    assert "node_capacity" in metrics
    assert metrics["failed_jobs"] >= 0
    assert metrics["deployment_ready"] in {True, False}

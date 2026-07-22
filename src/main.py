from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.collectors.kubernetes_metrics_collector import collect_kubernetes_metrics
from src.collectors.linux_metrics_collector import collect_linux_metrics
from src.collectors.service_health_collector import collect_service_health
from src.config import REPORTS_DIR
from src.reporting.csv_reporter import write_csv
from src.reporting.html_reporter import write_html
from src.reporting.json_reporter import write_json
from src.reporting.markdown_reporter import write_markdown


def generate_reports(output_dir: Path | None = None) -> dict:
    output_dir = output_dir or REPORTS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    linux_metrics = collect_linux_metrics()
    kubernetes_metrics = collect_kubernetes_metrics()
    service_health = collect_service_health()

    capacity_rows = [{
        "service": "trading-api-demo",
        "cpu_usage": linux_metrics["cpu_percent"],
        "memory_usage": linux_metrics["memory_percent"],
        "disk_usage": linux_metrics["disk_percent"],
        "pod_restarts": kubernetes_metrics["pods"][0]["restarts"],
        "risk_level": "Medium",
    }]

    performance_rows = [{
        "service": service_health["service"],
        "availability": service_health["availability_percent"],
        "response_time_ms": service_health["response_time_ms"],
        "failed_health_checks": service_health["failed_health_checks"],
        "status": service_health["status"],
    }]

    service_rows = [{
        "service": service_health["service"],
        "availability_percent": service_health["availability_percent"],
        "response_time_ms": service_health["response_time_ms"],
        "status": service_health["status"],
    }]

    capacity_report = write_csv(output_dir / "capacity_report.csv", capacity_rows)
    performance_report = write_csv(output_dir / "performance_report.csv", performance_rows)
    service_health_report = write_csv(output_dir / "service_health_report.csv", service_rows)
    weekly_summary = write_markdown(output_dir / "weekly_summary.md", "Weekly Summary", "Capacity and performance checks completed successfully.")
    executive_summary = write_html(output_dir / "executive_summary.html", "Executive Summary", "Infrastructure reporting workflow executed successfully.")
    write_json(output_dir / "report-metadata.json", {"linux": linux_metrics, "kubernetes": kubernetes_metrics, "service": service_health})

    return {
        "capacity_report.csv": capacity_report,
        "performance_report.csv": performance_report,
        "service_health_report.csv": service_health_report,
        "weekly_summary.md": weekly_summary,
        "executive_summary.html": executive_summary,
    }


if __name__ == "__main__":
    generate_reports()

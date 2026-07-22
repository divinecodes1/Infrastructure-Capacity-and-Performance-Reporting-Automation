from pathlib import Path

from src.main import generate_reports


def test_generate_reports_creates_expected_files(tmp_path):
    output_dir = tmp_path / "reports"
    generated = generate_reports(output_dir=output_dir)

    assert output_dir.joinpath("capacity_report.csv").exists()
    assert output_dir.joinpath("performance_report.csv").exists()
    assert output_dir.joinpath("service_health_report.csv").exists()
    assert output_dir.joinpath("weekly_summary.md").exists()
    assert output_dir.joinpath("executive_summary.html").exists()
    assert generated["capacity_report.csv"].exists()

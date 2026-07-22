# Infrastructure Capacity and Performance Reporting Automation

## Overview
This project demonstrates an automation-driven infrastructure reporting workflow for operational support, capacity planning, and performance monitoring. It combines Python, Ansible, Terraform, Jenkins, Vault, Kubernetes, Linux, and Grafana into a reusable platform that simulates how an IT architecture or infrastructure engineering team could produce recurring operational reports for a production-like environment.

## Why This Project
Modern infrastructure teams need dependable visibility into system health, capacity trends, service readiness, and performance risks. This project addresses that requirement by automating the collection of operational metrics, producing structured reports, and documenting the supporting architecture and operational processes.

## Key Features
- Linux and Kubernetes metric collection for capacity and service health
- Python-based report generation into CSV, Markdown, HTML, and JSON formats
- Ansible playbooks for operational support tasks and system checks
- Terraform-based infrastructure validation for a demo environment
- Jenkins pipeline automation for validation, testing, and report publishing
- Vault-based secret handling patterns for secure automation workflows
- Docker and Kubernetes deployment examples for scheduled reporting
- Grafana dashboard design for infrastructure visibility
- Architecture documentation, operational models, and runbooks

## Architecture
The solution is organized around a repeatable reporting lifecycle:

1. Terraform defines or validates the target infrastructure baseline.
2. Ansible performs operational support checks and system-level automation tasks.
3. Python collectors gather Linux, Kubernetes, and service health metrics.
4. The reporting engine produces capacity and performance outputs.
5. Jenkins runs validation and report generation as part of a CI/CD workflow.
6. Kubernetes and Docker provide deployment options for recurring execution.
7. Grafana and documentation assets provide operational visibility and support.

```text
Terraform / Ansible / Jenkins
           │
           ▼
Linux / Kubernetes Demo Environment
           │
           ▼
Python Metrics Collection
           │
           ▼
Reporting Engine
           │
           ▼
CSV / Markdown / HTML Reports + Grafana Dashboard
```

## Repository Structure
- src/: Python collectors, configuration, and report generation logic
- ansible/: operational playbooks and inventory
- terraform/: base infrastructure definitions and validation files
- k8s/: Kubernetes namespace, deployment, service, and CronJob manifests
- vault/: Vault policy and secret-handling documentation
- dashboards/: Grafana dashboard definition
- docs/: architecture, runbook, operational, and troubleshooting documentation
- reports/: generated capacity and performance reports

## Tech Stack
- Python
- Ansible
- Terraform
- Jenkins
- Vault
- Kubernetes
- Docker
- Linux / RHEL-compatible environments
- Grafana
- Git

## Local Setup
```bash
python -m pip install -r requirements.txt
pytest
python src/main.py
```

## Running with Docker
```bash
docker build -t capacity-reporter .
docker run --rm capacity-reporter
```

## Running with Docker Compose
```bash
docker compose up --build
```

## Jenkins Pipeline
The included Jenkins pipeline performs the following stages:
- Checkout
- Test execution
- Report generation
- Artifact archival

## Vault Secret Handling
The repository includes example documentation and policy files for Vault-based secret management. Real credentials are not committed to the repository.

## Reports and Outputs
Generated outputs are written to the reports directory and include:
- capacity_report.csv
- performance_report.csv
- service_health_report.csv
- weekly_summary.md
- executive_summary.html

## Documentation
The documentation set includes:
- architecture.md
- operational-model.md
- capacity-reporting-model.md
- performance-reporting-model.md
- runbook.md
- troubleshooting-guide.md

## Project Summary
This project is designed to support a strong interview and portfolio narrative for infrastructure engineering, platform operations, and automation-focused roles. It highlights practical experience with operational support workflows, automation, infrastructure documentation, reporting, and secure configuration handling.

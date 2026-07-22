# Infrastructure Capacity and Performance Reporting Automation

## Overview
This project automates infrastructure capacity and performance reporting using Python, Ansible, Terraform, Jenkins, Vault, Kubernetes, Linux, and Grafana.

## Why This Project
Infrastructure teams need recurring visibility into system health, capacity trends, service readiness, and performance risks. This project simulates an operational reporting workflow for cloud and Kubernetes-based infrastructure.

## Features
- Linux capacity metrics collection
- Kubernetes health and resource reporting
- Python-based report generation
- Ansible operational automation
- Terraform infrastructure validation
- Jenkins CI/CD pipeline
- Vault-based secret handling
- Dockerized report generator
- Kubernetes CronJob deployment
- Grafana dashboard
- Architecture diagrams and operational runbooks

## Running Locally
```bash
python -m pip install -r requirements.txt
pytest
python src/main.py
```

## Reports
Generated reports are written to the reports directory.

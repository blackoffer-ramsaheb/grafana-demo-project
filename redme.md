# Grafana Monitoring Dashboard

## Overview

This project demonstrates a basic server monitoring dashboard using Grafana, Prometheus, and Python.

The application collects system metrics such as CPU and Memory usage, exposes them through a Prometheus metrics endpoint, and visualizes them using Grafana dashboards.

## Features

* CPU Usage Monitoring
* Memory Usage Monitoring
* Prometheus Metrics Collection
* Grafana Dashboard Visualization
* Real-Time Monitoring

## Tech Stack

* Python
* Prometheus
* Grafana
* Docker
* psutil

## Project Structure

grafana-demo-project/

├── metrics.py

├── prometheus.yml

├── requirements.txt

├── README.md

└── screenshots/

## Setup

### Install Dependencies

pip install -r requirements.txt

### Run Metrics Server

python metrics.py

### Run Prometheus

docker run -d --name prometheus -p 9090:9090 -v <path_to_prometheus.yml>:/etc/prometheus/prometheus.yml prom/prometheus

### Run Grafana

docker run -d --name grafana -p 3000:3000 grafana/grafana

## Dashboard Panels

* CPU Usage Trend
* Memory Usage
* System Health

## Screenshots

Add screenshots of:

* Prometheus Targets Page
* Grafana Dashboard
* Prometheus Data Source Connection

## Learning Outcomes

* Understanding Prometheus metric collection
* Creating Grafana dashboards
* Monitoring system resources using Python
* Connecting Grafana with Prometheus

## Author

Ramsaheb Prasad

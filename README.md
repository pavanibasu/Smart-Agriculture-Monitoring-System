# Smart Agriculture Monitoring System using AWS IoT Core

## Project Overview
This project implements a distributed monitoring system for agricultural environments to track soil moisture, temperature, and humidity. Sensor data is generated using a Python-based simulator and securely transmitted to AWS IoT Core using MQTT over TLS. The data is stored, visualized, and monitored using AWS CloudWatch dashboards and alerts.

The system demonstrates an end-to-end IoT pipeline commonly used in real-world smart agriculture applications.

---

## Architecture
Sensor Simulator (Python)  
→ MQTT over TLS  
→ AWS IoT Core  
→ AWS IoT Rules  
→ CloudWatch Logs & Metrics  
→ CloudWatch Dashboard & Alerts  

---

## Features
- Simulated sensor readings for:
  - Temperature
  - Humidity
  - Soil Moisture
- Secure MQTT communication using X.509 certificates
- AWS IoT Core integration
- Time-series visualization using CloudWatch dashboards
- Threshold-based alerts using CloudWatch Alarms and SNS

---

## Technologies Used
- Python 3
- AWS IoT Core
- MQTT (TLS-secured)
- AWS CloudWatch (Logs, Metrics, Dashboards, Alarms)
- AWS SNS
- AWS CLI

---

## How It Works
1. A Python script simulates sensor data at regular intervals.
2. The data is published securely to AWS IoT Core using MQTT.
3. AWS IoT Rules route the data to CloudWatch Logs.
4. Metric filters extract numerical values from logs.
5. CloudWatch dashboards visualize real-time trends.
6. CloudWatch alarms trigger notifications when thresholds are crossed.

---

## How to Run
```bash
pip install paho-mqtt
python sensor_simulator_mqtt.py

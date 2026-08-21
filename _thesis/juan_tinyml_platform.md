---
title: "End-to-End Cloud-to-IoT Management Platform for TinyML Lifecycles"
supervisor: "Juan Aznar Poveda"
weight: 1
desired_skills: "Cloud Computing, IoT & LoRaWAN, TinyML, MLOps, Python / C++"
master: true
short: "Designing and evaluating an end-to-end MLOps platform for training, monitoring, versioning, and deploying TinyML updates across constrained IoT fleets."
number_of_students: "1–2 (preferred)"
language: "English"
new: true
---

This project focuses on the complete lifecycle management of Machine Learning models (TinyML) deployed across resource-constrained Internet of Things (IoT) devices. While training models at the cloud or edge is increasingly common, managing their deployment, monitoring performance, handling incremental versioning, and executing Firmware Updates Over-The-Air (FUOTA) under strict network limitations (such as LoRaWAN constraints) remains a major architectural challenge. Students will design and implement an end-to-end management platform that bridges cloud-based MLOps pipelines with constrained IoT hardware fleets.

### Focus

Designing, implementing, and evaluating a holistic Cloud-to-IoT MLOps and management platform. Emphasis on automated model versioning, delta-based updates over resource-constrained networks, fleet-wide monitoring, and orchestrating the entire TinyML lifecycle from cloud training to edge execution.

### Tasks

- **Platform Architecture:** Design a centralized cloud/edge management service that coordinates model training, version control, and packaging for resource-constrained targets. 
- **Efficient Update Mechanism:** Implement or integrate delta-based update strategies (e.g., incremental model weights) optimized for constrained transmission protocols like LoRaWAN FUOTA. 
- **Fleet Monitoring & Observability:** Build telemetry and monitoring loops to track device-level resource constraints, inference performance, and model drift across distributed IoT fleets. 
- **Evaluation & Benchmarking:** Deploy the platform across a testbed combining cloud services and physical or simulated constrained nodes, quantifying update delivery times, bandwidth consumption, and resource overhead.

### Required Skills

**Theoretical Skills:**

- MLOps and Machine Learning Lifecycle Management 
- Constrained Device Computing & TinyML Concepts 
- IoT Networking Protocols (LoRaWAN / FUOTA)

**Practical Skills:**

- Full-stack development (Python, C/C++ for microcontrollers)
- Cloud deployment and containerization (Docker, Kubernetes)
- Experience with embedded ML frameworks (e.g., TensorFlow Lite for Microcontrollers)
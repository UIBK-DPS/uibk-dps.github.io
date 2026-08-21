---
title: "eBPF-Driven Adaptive LLM Inference Under Resource Constraints"
supervisor: "Juan Aznar Poveda"
weight: 1
desired_skills: "Systems Programming, eBPF, Machine Learning Inference, C++ / Python"
master: true
short: "Investigating automated eBPF telemetry to dynamically adapt ONNX Runtime LLM inference strategies under resource-constrained environments."
number_of_students: "1–2 (preferred)"
language: "English"
new: true
---

This project explores the intersection of operating system observability and machine learning systems. Students will investigate the performance tradeoffs of Large Language Model (LLM) inference when subjected to resource-constrained environments (e.g., CPU throttling, memory pressure, or shared container limits). Using eBPF (Extended Berkeley Packet Filter), the project aims to build an automated feedback control loop that monitors kernel-level metrics and dynamically adjusts ONNX Runtime parameters or model variants to preserve performance SLAs.

### Focus

Designing and evaluating non-intrusive, OS-level monitoring architectures for AI workloads. Emphasis on leveraging eBPF telemetry to detect resource bottlenecks instantly and triggering runtime adaptations—such as dynamic thread pool tuning, quantization switching, or load shedding—for ONNX-based LLM deployments.

### Tasks

- **Telemetry & Monitoring:** Implement eBPF probes (uprobes and tracepoints) to measure inference latency distributions and OS-level thread scheduling delays.
- **Adaptive Control Loop:** Build a lightweight user-space controller that maps kernel-level resource saturation to inference configuration changes.
- **Performance Evaluation:** Benchmark ONNX Runtime LLM execution under artificial resource contention to evaluate the effectiveness and overhead of the automated adaptation strategy.

### Required Skills

**Theoretical Skills:**

- Operating Systems & Kernel Concepts 
- Performance Modeling & Profiling 
- Machine Learning Inference Tradeoffs (Latencies vs. Precision)

**Practical Skills:**  
- Programming in C++ and Python 
- Experience with eBPF (BCC or libbpf)
- Familiarity with ONNX Runtime and containerized environments (Docker/Linux)
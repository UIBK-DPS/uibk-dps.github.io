---
title: "Predictive Telemetry for Realistic Application Workloads"
supervisor: "Juan Aznar Poveda and Marlon Etheredge"
weight: 1
desired_skills: "Systems Programming, eBPF, Distributed Systems, Rust / C++ / Python"
master: false
short: "Distributed telemetry framework to capture and adapt to fine-grained application-level metrics using advanced eBPF tracing."
number_of_students: "1–2 (preferred)"
language: "English"
new: true
---

This project serves as an advanced extension of a distributed telemetry framework developed by the Distributed and Parallel Systems Group. While current telemetry systems primarily focus on system-level metrics (such as CPU accounting modes and network interfaces), modern distributed applications demand deep observability into complex workloads, microservices, and container runtimes. Students will extend the framework's eBPF-based instrumentation subsystem to collect fine-grained, low-overhead application metrics and evaluate how predictive data suppression and distributed aggregation perform under these high-frequency, complex application-level telemetry streams.

### Focus

Designing, implementing, and evaluating extensions to the telemetry framework for application-level eBPF tracing. Emphasis on minimizing probe overhead, handling high-cardinality metrics, and evaluating the effectiveness of predictive data reduction algorithms (e.g., LSTM-based suppression) on non-stationary, bursty application workloads in a Kubernetes environment.

### Tasks

- Kernel-Space Extension: Extend the framework's eBPF probes (using Rust and Aya) to track application-level events (e.g., system calls, thread synchronization delays, or socket-level request latencies).
- Pipeline Integration: Integrate the new fine-grained telemetry streams into \mn{}'s existing collection, discovery, and coordination layers without violating node resource constraints.
- Evaluation & Benchmarking: Deploy the extended framework on a Kubernetes testbed, comparing network bandwidth savings, prediction accuracy (MAE/MAPE), and aggregator resource overhead against traditional collection mechanisms.

### Required Skills

**Theoretical Skills:**

- Advanced Operating Systems & Kernel Tracing Concepts 
- Time-Series Analysis & Predictive Modeling 
- Distributed Systems & Cluster Observability

** Practical Skills:**

- Systems programming in Rust and Python 
- Experience with eBPF (Aya, BCC, or libbpf)
- Containerized environments (Kubernetes, Docker)
---
title: "Celerity"
date: 2026-08-12T12:00:00+02:00
icon: "/images/projects/icons/celerity.png"
weight: 3
---


The **Celerity project** provides a high-level C++20 API and runtime environment for programming distributed-memory accelerator clusters. Built on the Khronos SYCL standard, Celerity allows developers to scale data-parallel applications from a single accelerator to multiple GPU-equipped nodes without exposing explicit ranks or requiring manual work and data partitioning. The runtime derives dependencies from the program's data-access patterns and coordinates distributed execution behind the scenes.

<img src="/images/projects/celerity.svg" alt="Celerity logo" width="400"/>

**🌐 Project website:**  
[https://celerity.github.io/](https://celerity.github.io/)

# Objectives

Celerity's core mission is to make **high-performance distributed accelerator computing accessible through a familiar, expressive C++ interface** while retaining the scalability required by modern HPC applications.

Key objectives include:

1. **Transparent application scaling** across distributed-memory accelerator nodes without requiring developers to manage ranks or explicitly partition work.  
2. **Automatic data distribution and movement** based on declared buffer-access patterns, ensuring that each computation receives the data it needs.  
3. **Asynchronous, dataflow-driven execution** through task and command graphs that expose dependencies and enable efficient scheduling.  
4. Maintaining a **SYCL-oriented programming model** that eases adoption and supports vendor-independent accelerator programming.  

## Relevance

GPU clusters offer enormous computing power, but conventional distributed programming requires expertise in communication, synchronization, device management, and data placement. This complexity makes applications harder to develop, maintain, and move between cluster configurations.

> Celerity provides a **single-source programming model** that separates application logic from the mechanics of distributed accelerator execution.

The Celerity ecosystem provides:
- **Virtualized distributed buffers and range mappers** that describe how parallel computations access data.  
- **Automatic work partitioning and data transfers** that preserve a consistent application-level view across cluster nodes.  
- A **distributed scheduling architecture** in which each node constructs and executes only the locally relevant portion of the command graph.  
- **High-performance computing extensions to SYCL**, including cluster-wide reductions and collective host tasks.  

By combining high-level abstractions with asynchronous runtime scheduling, Celerity enables developers to create scalable accelerator applications while focusing on algorithms rather than low-level cluster coordination.

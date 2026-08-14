---
title: "UMUGUC"
date: 2026-08-12T12:00:00+02:00
icon: "/images/projects/icons/umuguc.png"
weight: 4
---


The **Usability-focused Multi-GPU Compression (UMUGUC) project** investigates how end-to-end data compression can be made practical for applications running on multi-GPU and distributed-memory systems. Compression can reduce memory-capacity and bandwidth bottlenecks, but integrating it throughout an application is complex and often couples the program to a particular compression method. UMUGUC addresses this barrier with a simple, declarative interface that leaves compression-specific implementation decisions to the runtime system.

<img src="/images/projects/umuguc.png" alt="UMUGUC logo" width="400"/>

**🌐 Project website:**  
[https://umuguc.github.io/](https://umuguc.github.io/)

# Objectives

UMUGUC's core mission is to **make compressed data easy to use throughout multi-GPU applications** without requiring developers to write compression and decompression logic for every data movement or storage operation.

Key objectives include:

1. Providing a **declarative extension to GPU buffer abstractions** for marking data as compressed and specifying quality constraints or a particular compression method.  
2. Enabling **automatic compression-strategy selection** based on application requirements, available hardware, memory constraints, and access granularity.  
3. Supporting **transparent compressed-data access** by generating the required movement, compression, and decompression operations for user kernels.  
4. Evaluating end-to-end compression with **data-intensive scientific and industrial workloads**, including airborne laser-mapping point-cloud processing.  

## Relevance

Large-scale GPU applications frequently move more data than their processors can consume efficiently. Keeping data compressed in memory and during transfers, then decompressing it close to the actual computation, can improve throughput, reduce capacity pressure, and lower the communication energy required. Implementing this manually, however, demands expertise in distributed systems, GPU optimization, and high-throughput compression.

> UMUGUC turns **end-to-end multi-GPU compression into a runtime-managed capability** rather than application-specific infrastructure.

The UMUGUC approach provides:
- **Compression-aware buffers** that allow developers to express functional precision and access requirements at a high level.  
- **Compile-time metaprogramming and runtime selection** of suitable compression implementations.  
- **Flexible decompression strategies** adapted to local and global memory limits and the access granularity of each method.  
- Integration with the **Celerity runtime and the SYCL programming model** for portable, data-parallel execution across accelerator systems.  

By making compression choices explicit but their implementation transparent, UMUGUC aims to bring the performance and efficiency benefits of compressed data processing to a much broader range of multi-GPU applications.

---
title: "CSM"
date: 2018-11-18T12:33:46+10:00
weight: 2
---


# A Unified Programming Model for the Computing Continuum

CSM is a framework for developing applications that operate seamlessly across cloud, edge, and IoT environments. Unlike component-centric models that often lead to fragmented architectures, CSM allows you to model an entire distributed system as a single, coherent entity. By managing coordination and state at a global level, the model simplifies orchestration and maintains architectural integrity across your infrastructure.

- Hierarchical System Design
CSM uses hierarchical nesting to manage complex application logic. By representing the application as a unified tree rather than isolated black boxes, the entire system topology remains visible. This enables the runtime to perform system-wide optimizations that are impossible in traditional architectures.
- Native Data Scoping
Data management is integrated into the model through explicit scoping rules. CSM categorizes variables as persistent (global), transient (local to a machine), or static (local to a state). Aligning code structure with memory placement reduces network synchronization and improves data efficiency.
- Decoupled Logic and Execution
Maintain a clean separation between high-level coordination and task execution. State machines handle logic and state transitions, while heavy processing and hardware I/O are offloaded to external services. These interactions are managed via declarative Invoke actions, keeping dependencies explicit.

CSM provides the system-wide visibility required for advanced resource optimization. By exposing the full application topology, the model supports automated scheduling and intelligent data placement across the continuum.

- CSML: A declarative DSL for specifying system behavior without the overhead of low-level communication boilerplate.
- Cirrina: An open-source, Kotlin-based runtime designed to manage state machine lifecycles from edge devices to cloud clusters.

CSM website: https://collaborativestatemachines.github.io/
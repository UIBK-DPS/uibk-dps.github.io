---
title: "CSM"
date: 2018-11-18T12:33:46+10:00
icon: "/images/projects/icons/csm.png"
weight: 2
---


The **Collaborative State Machines (CSM) project** introduces a unified programming model for developing applications across the Cloud–Edge–IoT continuum. As distributed applications become increasingly complex, existing component-centric approaches often result in fragmented architectures, making coordination, state management, and global optimization difficult. CSM addresses these challenges by enabling developers to model an entire distributed system as a single coherent entity, providing system-wide visibility and simplifying orchestration across heterogeneous computing environments.

**🌐 Project website:**  
[https://collaborativestatemachines.github.io/](https://collaborativestatemachines.github.io/)

# Objectives

The CSM project’s core mission is to **simplify the development and management of distributed applications** by providing a programming model that integrates coordination, state management, and execution across the computing continuum.

Key objectives include:

1. **Unified system modeling** enabling developers to describe complete distributed applications as a single hierarchical model rather than as isolated components.  
2. **Efficient state and data management** through explicit data scoping mechanisms that reduce unnecessary synchronization and improve data locality.  
3. **Separation of coordination and execution logic** by combining high-level state management with external services responsible for computation and hardware interaction.  
4. Providing a **runtime environment for continuum-scale applications** capable of managing distributed state machines from edge devices to cloud infrastructures.  

## Relevance

Modern cloud-edge-IoT applications require coordination among highly heterogeneous resources distributed across multiple administrative and geographical domains. Traditional programming approaches often expose developers to low-level communication mechanisms, fragmented application structures, and complex synchronization challenges.

> CSM provides a **system-level programming abstraction** for designing, executing, and optimizing distributed applications across the computing continuum.

The CSM ecosystem provides:
- A **hierarchical programming model** that represents distributed applications as a unified system structure, enabling global reasoning and optimization.  
- **Native data scoping mechanisms** for controlling data visibility and placement across global, local, and state-specific contexts.  
- **CSML, a declarative domain-specific language** for specifying application behavior without requiring low-level communication management.  
- **Cirrina, an open-source runtime environment** for managing state machine execution and coordination across edge and cloud infrastructures.  

By combining system-wide visibility, explicit state management, and flexible execution models, CSM enables the development of scalable, adaptable, and efficient applications for the next generation of distributed computing systems.
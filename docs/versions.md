# A11 Versions

This document tracks the main versions of **Algorithm 11 (A11)** across its core standard, applied models, and interface layers.

For full structural understanding, the **primary reference** is:

- **A11 — Structural Architecture Specification**  
  (see `/core/A11 — Structural Architecture Specification.pdf`, DOI: 10.5281/zenodo.18622044)

---

## A11 v1.0.x — Canonical Architecture (Stable)

**Status:** Stable, canonical  
**Scope:**

- universal deterministic reasoning architecture  
- cognitive model and reasoning loop  
- decision layer between perception and control  
- A11 Language for structured reasoning  
- integration requirements for engineering systems  
- architectural invariants and guarantees  

Defined in:

- `/core/A11 — Structural Architecture Specification.pdf`  
- `/core/A11 — Cognitive Architecture Specification.pdf`  
- `/core/A11 — Decision Layer Specification.pdf`  
- `/core/A11 — Language Specification.pdf`  
- `/core/A11 — System Integration Guide (v1.1).pdf`  
- `/core/A11 — Architectural Invariants.pdf`

---

## A11‑Lite v1.0.x — Operational Interface Layer

**Status:** Stable introductory and operational layer  
**Scope:**

- simplified L1–L11 structure for human–AI reasoning  
- activation and usage patterns for AI systems  
- conceptual guides (epistemology, cosmology, applications)  
- A11‑Agent interface for LLM‑based agents  

Defined in:

- `/lite/ALGORITHM_11.md`  
- `/lite/QUICK_START.md`  
- `/lite/A11‑AGENT.md`  
- `/lite/APPLICATIONS.md`  
- `/lite/EPISTEMOLOGY.md`  
- `/lite/COSMOLOGY.md`  
- `/lite/FAQ.md`  
- `/lite/agent/` (A11‑Agent engineering specs)

---

## Applied Models v1.0.x — Domain‑Specific Architectures

**Status:** Stable applied models (examples, not part of the core spec)  
**Scope:**

- autonomous vehicles — conflict resolution  
- multi‑agent robotics — coordination  
- off‑Earth construction — autonomous base building  

Defined in:

- `/applied/A11 for Autonomous Vehicles — Conflict Resolution Model.pdf`  
- `/applied/A11 for Multi‑Agent Robotics — Coordination Framework.pdf`  
- `/applied/A11 for Off‑Earth Construction — Autonomous Base Building.pdf`

---

## Practical Layer v1.0.x — Reference Case and Implementation

**Status:** Stable reference demonstration  
**Scope:**

- autonomous robot decision control in a partially unknown environment  
- full L1–L11 reasoning trace  
- minimal Python reference implementation  

Defined in:

- `/core_practical/case_autonomous_robot/CASE.md`  
- `/core_practical/case_autonomous_robot/STRUCTURE.md`  
- `/core_practical/case_autonomous_robot/TRACE_EXAMPLE.md`  
- `/core_practical/case_autonomous_robot/python_reference/`

---

## Future Versions (v2.x and Beyond)

Planned directions for future versions may include:

- extended multi‑agent and swarm reasoning models  
- advanced safety and verification layers  
- additional domain‑specific applied models  
- extended A11‑Agent capabilities and tooling  

All future changes will preserve the **core architectural invariants** defined in the Structural Architecture Specification.


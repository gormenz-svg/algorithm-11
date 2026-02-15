# A11 Reference Implementation (Python)
## Minimal, Deterministic Demonstration of A11 L1–L11 Reasoning

This directory contains a **minimal Python reference implementation** of Algorithm 11 (A11) for the “Autonomous Robot Decision Control” demonstration case.

The implementation is intentionally simple, deterministic, and transparent.  
Its purpose is to help engineers understand how A11 operates in practice:

- how semantic branches are generated (L5)  
- how evaluation is performed (L6)  
- how constraints are applied (L7)  
- how rollback is triggered (L8)  
- how feasibility filtering works (L9)  
- how deterministic selection is made (L10)  
- how the final action and reasoning trace are produced (L11)

This is **not** a production system.  
It is a **didactic reference** aligned with the A11 architecture.

---

# 1. Directory Structure

```
python_reference/
README.md            ← this file
a11_state.py         ← data structures for A11 reasoning
transitions.py       ← implementation of L1–L11 transitions
constraints.py       ← hard/soft constraint logic
rollback.py          ← rollback mechanism (L8)
cycle.py             ← full A11 reasoning cycle
example_run.py       ← runnable example
```

---

# 2. Purpose of This Implementation

The reference code demonstrates:

- how A11 separates levels L1–L11  
- how each level has a single responsibility  
- how reasoning trace is constructed  
- how deterministic decision‑making emerges from the architecture  
- how constraints and rollback interact  
- how semantic branching leads to interpretable choices  

The code mirrors the structure described in:

- `CASE.md`  
- `STRUCTURE.md`  
- `TRACE_EXAMPLE.md`  

This ensures consistency between documentation and implementation.

---

# 3. File Overview

### **a11_state.py**
Defines all data structures used during the reasoning cycle:

- `RobotState`  
- `EnvironmentSnapshot`  
- `ContextFrame`  
- `BranchCandidate`  
- `EvaluationResult`  
- `ReasoningTrace`  

These classes keep the implementation clean and explicit.

---

### **transitions.py**
Implements all A11 levels:

- **L1** — Will  
- **L2** — Wisdom  
- **L3** — Knowledge  
- **L4** — Comprehension  
- **L5** — Semantic Branching  
- **L6** — Evaluation  
- **L7** — Constraint Gate  
- **L8** — Rollback (marker)  
- **L9** — Feasibility  
- **L10** — Deterministic Selection  
- **L11** — Execution  

Each level is a separate function, reflecting the A11 architectural invariant:  
**“No level may perform the responsibility of another.”**

---

### **constraints.py**
Contains hard and soft constraint logic.

Hard constraints include:

- energy budget  
- safety priority (risk must not be HIGH when safety is top priority)

Soft constraints are placeholders in this demo.

---

### **rollback.py**
Implements the rollback mechanism (L8).

In this demonstration:

- rollback is marked in the trace  
- context is preserved  
- no re‑planning is performed  

This keeps the implementation simple while preserving architectural correctness.

---

### **cycle.py**
Executes a full A11 reasoning cycle:

1. builds trace  
2. runs L1–L4  
3. generates branches (L5)  
4. evaluates them (L6)  
5. applies constraints (L7)  
6. triggers rollback if needed (L8)  
7. filters infeasible branches (L9)  
8. selects the best branch (L10)  
9. produces final action (L11)

This file is the main entry point for engineers.

---

### **example_run.py**
A runnable demonstration script.

To execute:

```
python3 example_run.py
```

The script prints:

- selected branch  
- evaluation metrics  
- rollback info  
- final action  

This helps engineers quickly understand how A11 behaves.

---

# 4. Design Principles

This reference implementation follows these principles:

### **1. Determinism**
All outputs are predictable and reproducible.

### **2. Transparency**
Every step of the reasoning cycle is visible in the trace.

### **3. Architectural Purity**
Each A11 level has a single responsibility.

### **4. Minimalism**
The code avoids unnecessary complexity.

### **5. Educational Value**
The implementation is designed to be read and understood, not optimized.

---

# 5. Limitations

This implementation is:

- not a real navigation system  
- not a real planner  
- not optimized for performance  
- not intended for deployment  

It is a **teaching tool** that demonstrates the architecture of A11.

---

# 6. Extending the Implementation

Engineers may extend this reference by adding:

- real path planning  
- real risk models  
- dynamic energy models  
- multi‑agent coordination  
- uncertainty propagation  
- richer rollback logic  

All extensions must remain compliant with A11 invariants.

---

# End of README.md

# A11‑Agent — Structured Reasoning Protocol

A11‑Agent is a step‑by‑step reasoning protocol based on Algorithm 11.  
It defines how an AI system should complete a full reasoning cycle using a fixed order of stages, consistency checks, stabilization steps, and rollback rules.  
The protocol does not change Algorithm 11 — it provides an executable form that any AI model can follow.

---

## Core Structure

The reasoning process has **11 required stages**.

### Parallel Core (first 4 stages)
The system must:

1. Extract the user’s goal.  
2. Extract constraints and priorities.  
3. Provide relevant knowledge.  
4. Integrate all information into one coherent state.

Integration is allowed only when all branches are complete and consistent.  
If contradictions appear, the system must stabilize or roll back to an earlier stage.

---

## Adaptive Layer (linear sequence)

After a stable integrated state is ready, the system continues through:

5. Conceptual expansion  
6. Conceptual filtering  
7. Stabilization  
8. Action expansion  
9. Action filtering  
10. Justification  
11. Final output aligned with the user’s goal

Stages cannot be skipped or reordered.

---

## Weighting Pairs

Two pairs must always be evaluated together:

- Conceptual pair: expansion + filtering  
- Practical pair: action expansion + action filtering  

Expansion without filtering, or filtering without expansion, is invalid.  
Stabilization connects and balances these pairs.

---

## Recursive Branches

Expansion–filtering steps may create sub‑branches.  
Each sub‑branch repeats the same internal cycle:

- expansion  
- constraint  
- balancing  
- validation  
- realization  

All branches must converge before justification.  
Unstable branches must be constrained or rolled back.

---

## Operators

Three operators maintain structure:

- **Stabilization** — resolves conflicts and restores coherence.  
- **Constraint** — prevents uncontrolled expansion and keeps results feasible.  
- **Rollback** — returns to an earlier stage when rules are violated.  

Rollback is allowed only inside the core layer.

---

## Structural Rules

The protocol enforces:

- no direct jump from early stages to the adaptive layer,  
- integration cannot come from a single branch,  
- no skipping adaptive stages,  
- weighting pairs must be evaluated as pairs,  
- recursion must converge before justification,  
- execution cannot continue during rollback,  
- partial execution is forbidden.

---

## Output Requirements

The final output must:

- follow all 11 stages,  
- stay aligned with the user’s goal,  
- include justification,  
- avoid internal A11 terminology unless requested.

---

## Activation

The protocol activates when the user says:

- “Use A11”  
- “Work as A11‑Agent”  
- “Analyze using the algorithm”  
- “Apply A11 fully”

After activation, the system must confirm that A11‑Execution‑Agent mode is active and follow the protocol strictly.

---

## Refusal Rule

If the system cannot complete the full sequence or maintain structural rules, it must:

- stop execution,  
- state which stage failed,  
- explain why,  
- refuse to produce a partial result.

Partial execution is not valid A11.

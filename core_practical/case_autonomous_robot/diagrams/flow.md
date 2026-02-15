## FLOW DIAGRAM (L1–L11)
The full A11 stream as an engineering ASCII diagram

```
                     ┌──────────────────────────┐
                     │          L1 — WILL        │
                     │   Human intention origin   │
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │       L2 — WISDOM          │
                     │  Priorities & hard rules   │
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │      L3 — KNOWLEDGE        │
                     │  State, models, perception │
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │   L4 — COMPREHENSION       │
                     │  Single integration point  │
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │   L5 — SEMANTIC BRANCHING  │
                     │  A, B, C, D candidate paths│
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │      L6 — EVALUATION       │
                     │ scoring: risk, energy, etc │
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │   L7 — CONSTRAINT GATE     │
                     │  hard/soft constraints     │
                     └───────────────┬───────────┘
                                     │
                     │───────────────┘
                     │   if all fail → rollback
                     ▼
         ┌──────────────────────────┐
         │       L8 — ROLLBACK      │
         │ return to L4, rebuild    │
         └───────────────┬─────────┘
                         │
                         ▼
                     (back to L4)

                                     │
                     ┌───────────────▼───────────┐
                     │    L9 — FEASIBILITY        │
                     │ remove non-executable opts │
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │   L10 — ACTION SELECTION   │
                     │ deterministic choice rule  │
                     └───────────────┬───────────┘
                                     │
                     ┌───────────────▼───────────┐
                     │     L11 — EXECUTION        │
                     │  output + reasoning trace  │
                     └────────────────────────────┘
```

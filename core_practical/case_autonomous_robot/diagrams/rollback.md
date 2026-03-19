## ROLLBACK OPERATOR (A11)
Rollback is an operator, not a level. It restores stability when invariants fail.

                 ┌──────────────────────────┐
                 │     S7 — BALANCE         │
                 │  detects contradictions   │
                 └───────────────┬──────────┘
                                 │
                                 ▼
                     Invariants violated?
                     ┌───────────────┐
                     │     YES       │
                     └───────┬───────┘
                             │
                             ▼
                 ┌──────────────────────────┐
                 │     ROLLBACK OPERATOR    │
                 │  restore stable context  │
                 │  prune invalid branches  │
                 │  rebuild constraints     │
                 └───────────────┬──────────┘
                                 │
                                 ▼
                 ┌──────────────────────────┐
                 │  return to S1–S4 (Core)  │
                 │  rebuild comprehension    │
                 └──────────────────────────┘

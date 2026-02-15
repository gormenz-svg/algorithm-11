## ROLLBACK DIAGRAM (L8)
Shows how A11 reverts to L4 when invariants are violated

```
                 ┌──────────────────────────┐
                 │   L7 — CONSTRAINT GATE    │
                 └───────────────┬──────────┘
                                 │
                                 ▼
                     All branches FAIL?
                     ┌───────────────┐
                     │ YES           │
                     └───────┬───────┘
                             │
                             ▼
                 ┌──────────────────────────┐
                 │       L8 — ROLLBACK      │
                 │  restore stable context  │
                 │  adjust priorities       │
                 │  rebuild constraints     │
                 └───────────────┬──────────┘
                                 │
                                 ▼
                 ┌──────────────────────────┐
                 │   return to L4 — COMPREH │
                 │   rebuild context frame  │
                 └──────────────────────────┘
```

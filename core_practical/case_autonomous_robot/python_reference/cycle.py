# A11 Reference Implementation — Full Cycle (A11-Agent Compatible)
# Version 2.1 — L-marking preserved, architecture corrected

from a11_state import ReasoningTrace, ContextFrame
import transitions
import rollback


def run_cycle(mission, priorities, rules, env_snapshot, robot_state, models):
    trace = ReasoningTrace()

    # Save raw inputs for trace
    trace.inputs = {
        "mission": mission,
        "priorities": priorities,
        "rules": rules,
        "robot_state": {
            "position": robot_state.position,
            "energy": robot_state.energy,
        },
        "env": {
            "obstacles": env_snapshot.obstacles,
            "safety_zones": env_snapshot.safety_zones,
            "risk_zones": env_snapshot.risk_zones,
            "unknown_regions": env_snapshot.unknown_regions,
        },
    }

    # L1 — Will
    will = transitions.L1_will(mission)

    # L2 — Wisdom
    wisdom = transitions.L2_wisdom(priorities, rules)

    # L3 — Knowledge
    knowledge = transitions.L3_knowledge(env_snapshot, robot_state, models)

    # L4 — Comprehension (integration point)
    comp = transitions.L4_comprehension(wisdom, knowledge)

    context = ContextFrame(
        goal=mission["target"],
        safety_envelope=True,
        energy_envelope=robot_state.energy,
        obstacles=env_snapshot.obstacles,
        uncertainty=env_snapshot.unknown_regions
    )

    # -------------------------
    # PROJECTIVE PAIR (L5–L6)
    # -------------------------

    # L5 — Projective Freedom (semantic branching)
    branches = transitions.L5_projective_freedom(context)
    trace.branches = branches

    # L6 — Projective Constraint (conceptual filtering)
    branches = transitions.L6_projective_constraint(branches, context)

    # L7 — Balance (stabilize L5–L6)
    branches = transitions.L7_balance(branches, context)

    # -------------------------
    # PRACTICAL PAIR (L8–L9)
    # -------------------------

    # L8 — Practical Freedom (actionable options)
    branches = transitions.L8_practical_freedom(branches, context)

    # L9 — Practical Constraint (feasibility)
    branches = transitions.L9_practical_constraint(branches, context)
    trace.feasible = branches

    # L7 — Balance again (stabilize L8–L9)
    branches = transitions.L7_balance(branches, context)

    # -------------------------
    # ROLLBACK OPERATOR
    # -------------------------

    # If invariants fail → rollback to L1–L4
    if all(b.constraint_result is False for b in branches):
        context = rollback.rollback_operator(context, trace)
        return {"move_to": None, "reason": "rollback_no_feasible"}, trace

    # -------------------------
    # FINALIZATION
    # -------------------------

    # L10 — Foundation (structural grounding)
    foundation = transitions.L10_foundation(branches, context)

    # L11 — Realization (final output)
    action = transitions.L11_realization(foundation, trace)
    trace.selected = foundation
    trace.action = action

    return action, trace

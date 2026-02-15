# A11 Reference Implementation — Full Cycle
# Version 1.0

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

    # L1
    will = transitions.L1_will(mission)

    # L2
    wisdom = transitions.L2_wisdom(priorities, rules)

    # L3
    knowledge = transitions.L3_knowledge(env_snapshot, robot_state, models)

    # L4
    comp = transitions.L4_comprehension(wisdom, knowledge)
    context = ContextFrame(
        goal=mission["target"],
        safety_envelope=True,
        energy_envelope=robot_state.energy,
        obstacles=env_snapshot.obstacles,
        uncertainty=env_snapshot.unknown_regions
    )

    # L5
    branches = transitions.L5_branching(context)
    trace.branches = branches

    # L6
    branches = transitions.L6_evaluation(branches, context)

    # L7
    branches = transitions.L7_constraints(branches, context)

    # Check rollback condition: all hard constraints failed
    if all(b.constraint_result is False for b in branches):
        context = rollback.rollback_to_L4(context, trace)
        # В демо: после rollback просто возвращаем "нет действия"
        return {"move_to": None, "reason": "rollback_no_feasible"}, trace

    # L9
    branches = transitions.L9_feasibility(branches, context)
    trace.feasible = branches

    # L10
    selected = transitions.L10_selection(branches, context)
    trace.selected = selected

    # L11
    action = transitions.L11_execution(selected, trace)

    return action, trace

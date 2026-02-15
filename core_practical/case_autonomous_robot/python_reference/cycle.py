# A11 Reference Implementation — Full Cycle (Skeleton)
# Version 1.0

from a11_state import ReasoningTrace, ContextFrame
import transitions
import rollback

def run_cycle(mission, priorities, rules, env_snapshot, robot_state, models):
    trace = ReasoningTrace()

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

    # Check rollback condition
    if all(b.constraint_result is False for b in branches):
        context = rollback.rollback_to_L4(context, trace)
        return run_cycle(mission, priorities, rules, env_snapshot, robot_state, models)

    # L9
    branches = transitions.L9_feasibility(branches, context)

    # L10
    selected = transitions.L10_selection(branches, context)
    trace.selected = selected

    # L11
    action = transitions.L11_execution(selected, trace)
    trace.action = action

    return action, trace


# A11 Reference Implementation — Level Transitions
# Final demo version for autonomous robot case
# Version 1.0

from a11_state import BranchCandidate, EvaluationResult


def L1_will(mission):
    """Define intention."""
    return mission


def L2_wisdom(priorities, rules):
    """Define priorities and hard rules."""
    return {"priorities": priorities, "rules": rules}


def L3_knowledge(env_snapshot, robot_state, models):
    """Collect state, models, and environment."""
    return {"env": env_snapshot, "robot": robot_state, "models": models}


def L4_comprehension(wisdom, knowledge):
    """Integrate Wisdom + Knowledge into a context frame."""
    return {"wisdom": wisdom, "knowledge": knowledge}


def L5_branching(context):
    """
    Generate semantic branches:
    - A: shortest path
    - B: safest path
    - C: energy-optimal
    - D: exploration-biased
    """
    branches = [
        BranchCandidate(label="A_shortest", path=["SHORTEST_PATH"]),
        BranchCandidate(label="B_safest", path=["SAFEST_PATH"]),
        BranchCandidate(label="C_energy_optimal", path=["ENERGY_OPTIMAL_PATH"]),
        BranchCandidate(label="D_exploration", path=["EXPLORATION_PATH"]),
    ]
    return branches


def L6_evaluation(branches, context):
    """
    Evaluate each branch using simple deterministic metrics.
    This is a demonstration model, not a real planner.
    """

    for branch in branches:

        # Distance
        if "SHORTEST" in branch.label.upper():
            distance = 12
        elif "SAFEST" in branch.label.upper():
            distance = 18
        elif "ENERGY" in branch.label.upper():
            distance = 15
        else:
            distance = 20

        # Risk
        if "SAFEST" in branch.label.upper():
            risk = "LOW"
        elif "SHORTEST" in branch.label.upper():
            risk = "HIGH"
        else:
            risk = "MEDIUM"

        # Energy
        if "ENERGY" in branch.label.upper():
            energy = 10
        elif "SHORTEST" in branch.label.upper():
            energy = 12
        elif "SAFEST" in branch.label.upper():
            energy = 18
        else:
            energy = 20

        # Unknown exposure
        if "EXPLORATION" in branch.label.upper():
            unknown = "HIGH"
        elif "ENERGY" in branch.label.upper():
            unknown = "MEDIUM"
        else:
            unknown = "LOW"

        branch.evaluation = EvaluationResult(
            distance=distance,
            risk=risk,
            energy=energy,
            unknown_exposure=unknown
        )

    return branches


def L7_constraints(branches, context):
    """
    Apply hard and soft constraints.
    Hard:
      - energy must be <= energy_envelope
      - no 'HIGH' risk if safety is top priority
    Soft:
      - prefer lower risk, lower energy
    """
    energy_limit = context.energy_envelope
    safety_is_top = True  # в этом демо — да

    for branch in branches:
        ev = branch.evaluation
        hard_ok = True

        # Hard: energy budget
        if ev.energy > energy_limit:
            hard_ok = False

        # Hard: risk if safety is top
        if safety_is_top and ev.risk == "HIGH":
            hard_ok = False

        branch.constraint_result = hard_ok

    return branches


def L8_rollback(context, trace):
    """
    Rollback marker — в демо просто помечаем, что он был бы вызван.
    Реальная логика живёт в rollback.py и cycle.py.
    """
    trace.rollback_info = "rollback_triggered"
    return context


def L9_feasibility(branches, context):
    """
    Remove infeasible branches.
    В демо считаем:
      - ветка с unknown_exposure == HIGH считается нефизибельной.
    """
    feasible = []
    for b in branches:
        if b.evaluation.unknown_exposure == "HIGH":
            continue
        feasible.append(b)
    return feasible


def L10_selection(branches, context):
    """
    Deterministic selection:
      1) lowest risk
      2) then lowest energy
      3) then shortest distance
    """
    if not branches:
        return None

    def key(b):
        risk_order = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
        ev = b.evaluation
        return (
            risk_order.get(ev.risk, 3),
            ev.energy,
            ev.distance,
        )

    branches_sorted = sorted(branches, key=key)
    return branches_sorted[0]


def L11_execution(selected_branch, trace):
    """
    Produce final action and store trace.
    В демо: просто возвращаем символическое действие.
    """
    if selected_branch is None:
        action = {"move_to": None, "reason": "no_feasible_branch"}
    else:
        # В реальном кейсе здесь был бы следующий waypoint.
        action = {
            "move_to": "NEXT_WAYPOINT",
            "reason": f"selected {selected_branch.label}"
        }

    trace.action = action
    return action

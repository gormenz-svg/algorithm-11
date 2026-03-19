# A11 Reference Implementation — Level Transitions (A11-Agent Compatible)
# Version 2.0 — L-marking preserved

from a11_state import BranchCandidate, EvaluationResult


# -------------------------
# CORE LAYERS (L1–L4)
# -------------------------

def L1_will(mission):
    """Define intention (Will)."""
    return mission


def L2_wisdom(priorities, rules):
    """Define priorities and hard rules (Wisdom)."""
    return {"priorities": priorities, "rules": rules}


def L3_knowledge(env_snapshot, robot_state, models):
    """Collect state, models, and environment (Knowledge)."""
    return {"env": env_snapshot, "robot": robot_state, "models": models}


def L4_comprehension(wisdom, knowledge):
    """Integrate Wisdom + Knowledge (Comprehension)."""
    return {"wisdom": wisdom, "knowledge": knowledge}


# -------------------------
# PROJECTIVE PAIR (L5–L6–L7)
# -------------------------

def L5_projective_freedom(context):
    """
    Projective Freedom:
    Generate semantic options (conceptual branches).
    """
    return [
        BranchCandidate(label="A_shortest", path=["SHORTEST_PATH"]),
        BranchCandidate(label="B_safest", path=["SAFEST_PATH"]),
        BranchCandidate(label="C_energy_optimal", path=["ENERGY_OPTIMAL_PATH"]),
        BranchCandidate(label="D_exploration", path=["EXPLORATION_PATH"]),
    ]


def L6_projective_constraint(branches, context):
    """
    Projective Constraint:
    Apply conceptual constraints (not feasibility).
    Only conceptual filtering, no metrics.
    """
    filtered = []
    for b in branches:
        # Example conceptual constraint:
        # "exploration" allowed only if uncertainty exists
        if "EXPLORATION" in b.label.upper() and not context.uncertainty:
            continue
        filtered.append(b)
    return filtered


def L7_balance(branches, context):
    """
    Balance:
    Stabilize the pair (L5–L6) or (L8–L9).
    In demo: identity function.
    """
    return branches


# -------------------------
# PRACTICAL PAIR (L8–L9–L7)
# -------------------------

def L8_practical_freedom(branches, context):
    """
    Practical Freedom:
    Expand conceptual branches into actionable variants.
    In demo: attach simple metadata.
    """
    for b in branches:
        b.action_variants = ["MOVE", "WAIT"]
    return branches


def L9_practical_constraint(branches, context):
    """
    Practical Constraint:
    Feasibility filtering.
    In demo: remove branches with HIGH unknown exposure.
    """
    feasible = []
    for b in branches:
        # Unknown exposure is computed later in evaluation
        # so we skip filtering here; real logic is in L6/L7/L10.
        feasible.append(b)
    return feasible


# -------------------------
# EVALUATION + FOUNDATION + REALIZATION
# -------------------------

def L10_foundation(branches, context):
    """
    Foundation:
    Compute evaluation metrics and prepare structural grounding.
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


def L11_realization(branches, trace):
    """
    Realization:
    Deterministic selection + final action.
    """

    if not branches:
        action = {"move_to": None, "reason": "no_branches"}
        trace.action = action
        return action

    def key(b):
        risk_order = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
        ev = b.evaluation
        return (
            risk_order.get(ev.risk, 3),
            ev.energy,
            ev.distance,
        )

    selected = sorted(branches, key=key)[0]
    trace.selected = selected

    action = {
        "move_to": "NEXT_WAYPOINT",
        "reason": f"selected {selected.label}"
    }

    trace.action = action
    return action

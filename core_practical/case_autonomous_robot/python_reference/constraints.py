# A11 Reference Implementation — Constraints (A11-Agent Compatible)
# Version 2.0 — L-marking preserved

#
# IMPORTANT:
# In A11-Agent:
# - L6 = Projective Constraint  → conceptual filtering
# - L9 = Practical Constraint   → feasibility filtering
# This file provides both types of constraints.
#


# -------------------------
# PROJECTIVE CONSTRAINTS (L6)
# -------------------------

def projective_constraints(branch, context):
    """
    Conceptual (non-physical) constraints.
    These operate on semantic meaning, not metrics.

    Examples:
    - Exploration allowed only if uncertainty exists
    - Energy-optimal path allowed only if energy is relevant
    """

    label = branch.label.upper()

    # Exploration requires uncertainty
    if "EXPLORATION" in label and not context.uncertainty:
        return False

    # Energy-optimal path allowed only if energy envelope is tight
    if "ENERGY" in label and context.energy_envelope > 50:
        return False

    return True



# -------------------------
# PRACTICAL CONSTRAINTS (L9)
# -------------------------

def practical_constraints(evaluation, context, safety_is_top=True):
    """
    Practical (physical/feasibility) constraints.
    These operate on evaluation metrics.

    Hard constraints:
      - energy <= energy_envelope
      - if safety is top priority: risk != HIGH
    """

    # Energy feasibility
    if evaluation.energy > context.energy_envelope:
        return False

    # Safety feasibility
    if safety_is_top and evaluation.risk == "HIGH":
        return False

    return True



# -------------------------
# SOFT CONSTRAINTS (used in L10 Foundation)
# -------------------------

def soft_constraints(evaluation):
    """
    Soft constraints placeholder.
    Could return weights or scores; in this demo we don't modify anything.
    """
    return {}

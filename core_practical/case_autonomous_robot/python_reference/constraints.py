# A11 Reference Implementation — Constraints
# Version 1.0

def hard_constraints(evaluation, context, safety_is_top=True):
    """
    Hard constraints:
      - energy <= energy_envelope
      - if safety is top priority: risk != HIGH
    """
    if evaluation.energy > context.energy_envelope:
        return False

    if safety_is_top and evaluation.risk == "HIGH":
        return False

    return True


def soft_constraints(evaluation):
    """
    Soft constraints placeholder.
    Could return weights or scores; in this demo we don't modify anything.
    """
    return {}

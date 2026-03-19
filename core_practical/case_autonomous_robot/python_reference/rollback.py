# A11 Reference Implementation — Rollback Operator
# Version 2.0 (A11-Agent Compatible, L-marking preserved)

def rollback_operator(context, trace):
    """
    A11 Rollback Operator

    In A11:
    - Rollback is NOT a level (not L8)
    - It is invoked when invariants fail in L5–L11
    - It returns execution to the stable Core Layer (L1–L4)
    - It restores or resets the context frame

    In this demonstration:
    - We only mark that rollback occurred
    - Context is returned unchanged for simplicity
    """

    trace.rollback_info = {
        "status": "rollback_triggered",
        "returned_to": "L1-L4_core_layer"
    }

    return context

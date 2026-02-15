# A11 Reference Implementation — Rollback Logic
# Version 1.0

def rollback_to_L4(context, trace):
    """
    Rollback must:
    - mark that rollback was triggered
    - in real system: adjust context/priorities/envelopes
    In this demo we only mark it in the trace.
    """
    trace.rollback_info = "rollback_triggered"
    return context

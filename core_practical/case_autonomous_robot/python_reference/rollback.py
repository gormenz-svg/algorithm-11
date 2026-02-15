# A11 Reference Implementation — Rollback Logic (Skeleton)
# Version 1.0

def rollback_to_L4(context, trace):
    """
    Rollback must:
    - restore stable context
    - adjust priorities or envelopes if needed
    - never skip L4
    """
    trace.rollback_info = "rollback_triggered"
    return context


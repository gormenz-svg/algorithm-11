# A11 Reference Implementation — State Structures
# Version 2.1 (A11-Agent Compatible, L-marking preserved)

class RobotState:
    """
    Physical and mission-related robot state.
    Used in L3 (Knowledge).
    """
    def __init__(self, position, energy, orientation=None):
        self.position = position
        self.energy = energy
        self.orientation = orientation


class EnvironmentSnapshot:
    """
    Environment data available at the current cycle.
    Also part of L3 (Knowledge).
    """
    def __init__(self, obstacles, safety_zones, risk_zones, unknown_regions):
        self.obstacles = obstacles
        self.safety_zones = safety_zones
        self.risk_zones = risk_zones
        self.unknown_regions = unknown_regions


class ContextFrame:
    """
    Context frame constructed at L4 (Comprehension).
    Integrates Wisdom + Knowledge into a stable planning envelope.
    """
    def __init__(self, goal, safety_envelope, energy_envelope, obstacles, uncertainty):
        self.goal = goal
        self.safety_envelope = safety_envelope
        self.energy_envelope = energy_envelope
        self.obstacles = obstacles
        self.uncertainty = uncertainty


class BranchCandidate:
    """
    Semantic branch generated at L5 (Projective Freedom).
    Evaluation and constraint results are filled in later levels.
    """
    def __init__(self, label, path):
        self.label = label
        self.path = path
        self.evaluation = None
        self.constraint_result = None
        self.action_variants = None  # added for L8 practical freedom


class EvaluationResult:
    """
    Evaluation metrics computed at L10 (Foundation).
    L6 and L9 do not compute metrics — they only filter.
    """
    def __init__(self, distance, risk, energy, unknown_exposure):
        self.distance = distance
        self.risk = risk
        self.energy = energy
        self.unknown_exposure = unknown_exposure


class ReasoningTrace:
    """
    Full reasoning trace for one A11 cycle.
    Stores all intermediate states for transparency.
    """
    def __init__(self):
        self.inputs = {}
        self.branches = []
        self.evaluations = []
        self.constraints = []
        self.rollback_info = None
        self.feasible = []
        self.selected = None
        self.action = None

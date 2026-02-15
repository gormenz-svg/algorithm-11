# A11 Reference Implementation — State Structures
# Version 1.0

class RobotState:
    """Holds robot's physical and mission-related state."""
    def __init__(self, position, energy, orientation=None):
        self.position = position
        self.energy = energy
        self.orientation = orientation


class EnvironmentSnapshot:
    """Holds environment data available at the current cycle."""
    def __init__(self, obstacles, safety_zones, risk_zones, unknown_regions):
        self.obstacles = obstacles
        self.safety_zones = safety_zones
        self.risk_zones = risk_zones
        self.unknown_regions = unknown_regions


class ContextFrame:
    """Constructed at L4 — integrates Wisdom + Knowledge."""
    def __init__(self, goal, safety_envelope, energy_envelope, obstacles, uncertainty):
        self.goal = goal
        self.safety_envelope = safety_envelope
        self.energy_envelope = energy_envelope
        self.obstacles = obstacles
        self.uncertainty = uncertainty


class BranchCandidate:
    """Represents a semantic branch generated at L5."""
    def __init__(self, label, path):
        self.label = label
        self.path = path
        self.evaluation = None
        self.constraint_result = None


class EvaluationResult:
    """Evaluation metrics computed at L6."""
    def __init__(self, distance, risk, energy, unknown_exposure):
        self.distance = distance
        self.risk = risk
        self.energy = energy
        self.unknown_exposure = unknown_exposure


class ReasoningTrace:
    """Full reasoning trace for one A11 cycle."""
    def __init__(self):
        self.inputs = {}
        self.branches = []
        self.evaluations = []
        self.constraints = []
        self.rollback_info = None
        self.feasible = []
        self.selected = None
        self.action = None

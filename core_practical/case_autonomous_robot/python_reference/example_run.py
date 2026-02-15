# A11 Reference Implementation — Example Run (Skeleton)
# Version 1.0

from cycle import run_cycle
from a11_state import RobotState, EnvironmentSnapshot

def main():
    mission = {"target": (10, 10)}
    priorities = ["safety", "mission", "energy", "exploration"]
    rules = {"avoid_safety_zones": True}

    robot = RobotState(position=(3, 4), energy=27)
    env = EnvironmentSnapshot(
        obstacles=[(5,4), (6,4)],
        safety_zones=[(4,6), (5,6)],
        risk_zones=[(7,7)],
        unknown_regions=[(6,8)]
    )

    models = {"energy_cost": 1}

    action, trace = run_cycle(mission, priorities, rules, env, robot, models)

    print("Selected action:", action)
    print("Trace:", trace.__dict__)

if __name__ == "__main__":
    main()


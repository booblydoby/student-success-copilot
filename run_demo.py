import json
import sys
from planner.bfs_planner import bfs_plan


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_demo.py data/demo_scenarios.json")
        return

    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        data = json.load(f)

    for scenario_name, scenario in data.items():
        print("\n==============================")
        print(f"Scenario: {scenario_name}")
        print("==============================")

        user = scenario["user"]
        tasks = scenario["tasks"]

        schedule = bfs_plan(user, tasks)

        if schedule is None:
            print("No valid schedule found.")
        else:
            print("\nWeekly Plan:")
            for day, assignments in schedule.items():
                if assignments:
                    print(f"{day}: {len(assignments)} hour(s) -> {assignments}")
                else:
                    print(f"{day}: Free")


if __name__ == "__main__":
    main()
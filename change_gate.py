import sys
import yaml
import logging
from rules import validate_rules
from models import Decision


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


REQUIRED_FIELDS = ["action", "resource", "name", "environment"]

def load_config():
    try:
        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)
    except Exception:
        print("Error loading config.yaml")
        sys.exit(1)

def parse_input(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid YAML structure.")

        for field in REQUIRED_FIELDS:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        return data

    except FileNotFoundError:
        logging.error("File not found.")
        sys.exit(1)
    except yaml.YAMLError:
        logging.error("Invalid YAML format.")
        sys.exit(1)
    except Exception as e:
        logging.error(str(e))
        sys.exit(1)


def generate_plan(data: dict) -> list:
    plan = [
        f"Action: {data['action']}",
        f"Target: {data['resource']}/{data['name']}",
        f"Environment: {data['environment']}",
    ]

    if data["action"] == "scale":
        plan.append(f"Desired replicas: {data.get('replicas', 'Not specified')}")

    return plan


def decide(decision: Decision) -> int:
    if decision == Decision.BLOCKED:
        return 2
    if decision == Decision.APPROVAL_REQUIRED:
        return 1
    return 0



def main():
    if len(sys.argv) != 2:
        print("Usage: python change_gate.py <yaml_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    data = parse_input(file_path)
    config = load_config()
    plan = generate_plan(data) 
    messages, decision = validate_rules(data, config)
    
    
    print("\nPLAN:")
    for item in plan:
        print(f"- {item}")

    print("\nVALIDATION:")
    for msg in messages:
        print(f"- {msg}")

    print("\nRESULT:")
    print(decision.value)

    sys.exit(decide(decision))
    config = load_config()

if __name__ == "__main__":
    main()
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from rules import validate_rules
from models import Decision
import yaml

app = FastAPI(title="Production Change Approval API")


# -------- Request Model --------
class ChangeRequest(BaseModel):
    action: str
    resource: str
    name: str
    environment: str
    replicas: Optional[int] = None


# -------- Load Config --------
def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


# -------- Generate Plan --------
def generate_plan(data: dict) -> List[str]:
    plan = [
        f"Action: {data['action']}",
        f"Target: {data['resource']}/{data['name']}",
        f"Environment: {data['environment']}",
    ]

    if data["action"] == "scale":
        plan.append(f"Desired replicas: {data.get('replicas')}")

    return plan


# -------- API Endpoint --------
@app.get("/")
def home():
    return {"message": "Production Change Approval API is running"}


@app.post("/evaluate-change")
def evaluate_change(request: ChangeRequest):

    data = request.dict()
    config = load_config()

    plan = generate_plan(data)
    messages, decision = validate_rules(data, config)

    return {
        "plan": plan,
        "validation": messages,
        "result": decision.value
    }
from rules import validate_rules
from models import Decision


def test_delete_production_blocked():
    data = {
        "action": "delete",
        "resource": "deployment",
        "name": "test",
        "environment": "production",
    }
    _, decision = validate_rules(data)
    assert decision == Decision.BLOCKED


def test_scale_production_requires_approval():
    data = {
        "action": "scale",
        "resource": "deployment",
        "name": "test",
        "environment": "production",
        "replicas": 10,
    }
    _, decision = validate_rules(data)
    assert decision == Decision.APPROVAL_REQUIRED
from models import Decision


def validate_rules(data, config):
    action = data["action"]
    environment = data["environment"]
    replicas = data.get("replicas", 0)

    messages = []
    decision = Decision.AUTO_APPROVED

    # Rule 1
    if action == "delete" and environment == "production":
        messages.append("Deletion in production is strictly blocked.")
        decision = Decision.BLOCKED
        return messages, decision

    # Rule 2
    if action == "scale" and environment == "production":
        messages.append("Production environment detected.")
        if replicas > 5:
            messages.append(
                f"Replica count {replicas} exceeds safe threshold (5)."
            )
            decision = Decision.APPROVAL_REQUIRED
        return messages, decision

    # Rule 3
    if action == "apply" and environment == "staging":
        messages.append("Apply operation in staging is auto-approved.")
        return messages, decision

    messages.append("No policy violations detected.")
    return messages, decision
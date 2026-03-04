# Production Change Approval System

A CLI-based safety gate that enforces policy controls before allowing infrastructure changes.

This system simulates production-grade guardrails used in DevOps platforms to prevent unsafe operations.

---

## Design Philosophy

Built with:

- Clarity over cleverness
- Strict separation of concerns
- Deterministic rule evaluation
- Production-style logging
- Explicit decision modeling using Enums

---

## Architecture

User Input (YAML)
        ↓
Parse & Validate
        ↓
Generate Plan
        ↓
Apply Policy Rules
        ↓
Decision Engine
        ↓
Final Result + Exit Code

---

## Setup

1. Create virtual environment

python -m venv venv
venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

---

## Usage

python change_gate.py sample.yaml

---

## Exit Codes

0 → AUTO-APPROVED  
1 → APPROVAL REQUIRED  
2 → BLOCKED  

---

## Policy Rules Implemented

- Delete in production → BLOCKED
- Scale > 5 replicas in production → APPROVAL REQUIRED
- Apply in staging → AUTO-APPROVED
- All other safe cases → AUTO-APPROVED

---

## Engineering Decisions

- Rules isolated in rules.py for extensibility
- Enum-based decisions to avoid magic strings
- Structured error handling
- Deterministic output formatting
- Testable rule logic (pytest included)

---

## Assumptions

- Replica validation applies only to scale action
- Threshold fixed at 5
- YAML schema kept minimal for clarity

---

## Future Improvements

- Policy engine abstraction layer
- Configurable rule thresholds
- JSON schema validation
- Audit logging
- REST API wrapper
- GitHub Actions integration

---

Built as if it were shipping to production.
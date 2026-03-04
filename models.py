from enum import Enum


class Decision(Enum):
    AUTO_APPROVED = "AUTO-APPROVED"
    APPROVAL_REQUIRED = "APPROVAL REQUIRED"
    BLOCKED = "BLOCKED"
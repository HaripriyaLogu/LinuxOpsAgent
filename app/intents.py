from enum import Enum


class Intent(Enum):
    KNOWLEDGE = "knowledge"
    DIAGNOSTIC = "diagnostic"
    ACTION = "action"
    UNKNOWN = "unknown"
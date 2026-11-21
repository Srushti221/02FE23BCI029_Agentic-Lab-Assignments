"""Assignment 6B - Escalate after two failures using the audit log.
Name: Srushti Bandi | SRN: 02FE23BCI029
Assignment question: Add a rule: if the same skill fails twice in one session for the same user, the third attempt must escalate to a human instead of retrying the skill again. Implement this using the existing audit log (count prior error entries for that user/skill pair) rather than adding new hidden state. Submit the updated code and a transcript showing two failures followed by an escalation instead of a third attempt. 
"""
from datetime import datetime

class Memory:
    def __init__(self): self._store = {}
    def scope(self, user): return self._store.setdefault(user, {})

class Audit:
    def __init__(self): self.entries = []
    def log(self, user, task, skill_name, tool_calls, result=None, error=None):
        self.entries.append({"time": datetime.now().isoformat(timespec="seconds"), "user": user,
                             "task": task, "skill": skill_name, "tool_calls": tool_calls,
                             "result": result, "error": error})

class DraftEmailSkill:
    CONTACTS = {"Dr. Meena": "meena@example.edu"}
    def __init__(self, memory_scope): self.memory_scope, self.tool_calls = memory_scope, []
    def execute(self, task):
        contact = self.CONTACTS.get(task.get("contact"))
        self.tool_calls.append({"tool": "lookup_contact", "output": contact or {"error": "contact not found"}})
        if contact is None: raise RuntimeError(f"No contact found for {task.get('contact')}")
        return f"Draft created for {contact}: {task.get('subject', 'No subject')}"

SKILL_REGISTRY = {"draft_email": DraftEmailSkill}

def run_task(task, user, memory, audit):
    """Original runtime loop signature; failures are written to the audit log."""
    skill_name = task["skill"]
    skill = SKILL_REGISTRY[skill_name](memory.scope(user))
    try:
        result = skill.execute(task)
        audit.log(user, task, skill_name, skill.tool_calls, result=result)
        print("SUCCESS:", result)
        return result
    except Exception as error:
        audit.log(user, task, skill_name, skill.tool_calls, error=str(error))
        print("FAILED:", error)
        return None

def receive_task(task, user, memory, audit):
    skill_name = task["skill"]
    # The decision is derived only from existing audit entries for this user/skill.
    prior_failures = sum(1 for entry in audit.entries
                         if entry["user"] == user and entry["skill"] == skill_name
                         and entry["error"] is not None)
    if prior_failures >= 2:
        message = f"HUMAN ESCALATION: {skill_name} has failed twice for {user}; third execution was not attempted."
        print(message)
        audit.log(user, task, skill_name, [], error="escalated to human; retry blocked")
        return {"escalated": True, "message": message}
    run_task(task, user, memory, audit)
    return {"escalated": False}

if __name__ == "__main__":
    memory, audit = Memory(), Audit()
    task = {"skill": "draft_email", "contact": "Unknown Person", "subject": "Lab update"}
    for attempt in range(1, 4):
        print(f"\nAttempt {attempt}:")
        receive_task(task, "student_01", memory, audit)
    print("\nActual skill failures:", sum(e["error"] and not e["error"].startswith("escalated") for e in audit.entries))
    print("Audit records:", len(audit.entries))

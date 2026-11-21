"""Assignment 6A - Per-user task limit in the existing runtime pattern.
Name: Srushti Bandi | SRN: 02FE23BCI029
Assignment question: Add a new control: each user may run at most 3 tasks per session. Implement this as a check inside `receive_task` (or a thin wrapper around it) without changing `run_task`'s core loop signature or its skill-dispatch logic. Submit the updated code and a transcript showing a 4th task being rejected. 
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

class SummarizeNotesSkill:
    def __init__(self, memory_scope): self.memory_scope, self.tool_calls = memory_scope, []
    def execute(self, task):
        words = len(task.get("text", "").split())
        self.tool_calls.append({"tool": "word_count", "output": {"count": words}})
        self.memory_scope["last_note_length"] = words
        return f"Summary prepared for {words} words."

class TranslateTextSkill:
    def __init__(self, memory_scope): self.memory_scope, self.tool_calls = memory_scope, []
    def execute(self, task):
        result = f"[Translated to {task.get('language', 'English')}] {task.get('text', '')}"
        self.tool_calls.append({"tool": "translation_stub", "output": result})
        return result

SKILL_REGISTRY = {"summarize": SummarizeNotesSkill, "translate": TranslateTextSkill}

def run_task(task, user, memory, audit):
    """Original runtime loop signature and registry-based dispatch are retained."""
    skill_name = task["skill"]
    if skill_name not in SKILL_REGISTRY:
        error = f"Unknown skill: {skill_name}"
        audit.log(user, task, skill_name, [], error=error)
        raise ValueError(error)
    skill = SKILL_REGISTRY[skill_name](memory.scope(user))
    try:
        result = skill.execute(task)
        audit.log(user, task, skill_name, skill.tool_calls, result=result)
        return result
    except Exception as error:
        audit.log(user, task, skill_name, skill.tool_calls, error=str(error))
        raise

class Runtime:
    def __init__(self):
        self.memory, self.audit = Memory(), Audit()
        self.task_counts = {}  # per-user counts for this runtime session
    def receive_task(self, task, user):
        count = self.task_counts.get(user, 0)
        if count >= 3:
            message = f"Rejected: {user} has reached the maximum of 3 tasks in this session."
            print(message)
            self.audit.log(user, task, task.get("skill", "unknown"), [], error="session task limit reached")
            return {"accepted": False, "message": message}
        self.task_counts[user] = count + 1
        result = run_task(task, user, self.memory, self.audit)
        print(result)
        return {"accepted": True, "result": result}

if __name__ == "__main__":
    runtime = Runtime()
    tasks = [
        {"skill": "summarize", "text": "Agents use tools and memory."},
        {"skill": "translate", "text": "Hello team", "language": "Kannada"},
        {"skill": "summarize", "text": "A goal directs an agent."},
        {"skill": "translate", "text": "This fourth task must be blocked", "language": "Hindi"},
    ]
    for number, task in enumerate(tasks, 1):
        print(f"\nTask {number}:")
        runtime.receive_task(task, "student_01")
    print("\nAccepted task count:", runtime.task_counts["student_01"])
    print("Successful task audit entries:", sum(e["error"] is None for e in runtime.audit.entries))

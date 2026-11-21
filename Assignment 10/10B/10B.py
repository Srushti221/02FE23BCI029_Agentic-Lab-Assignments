"""Assignment 10B - Safe auto-remediation with rollback approval gate.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a WARNING-level (not ALARM/degraded-critical) scenario where the proposed action is a low-risk `restart_single_pod`. Demonstrate that this low-risk action is allowed to execute automatically (per `risk_level`), while any rollback-class action anywhere in your extended code still always routes through the approval-request path and never auto-executes.
"""
def request_approval(action, reason):
    return {"status": "approval_required", "action": action, "reason": reason}

def remediate(severity, action, risk_level):
    # Rollback is always approval-gated, regardless of severity or risk label.
    if "rollback" in action.lower():
        return request_approval(action, "Rollback-class actions always require human approval.")
    if severity == "WARNING" and action == "restart_single_pod" and risk_level == "low":
        return {"status": "auto_executed", "action": action,
                "reason": "WARNING-level incident and explicitly low-risk single-pod restart."}
    return request_approval(action, "Action is not eligible for automatic execution.")

if __name__ == "__main__":
    tests = [
        ("WARNING", "restart_single_pod", "low"),
        ("WARNING", "rollback_deployment", "low"),
        ("ALARM", "restart_single_pod", "low"),
        ("WARNING", "rollback_deployment", "high"),
    ]
    for severity, action, risk in tests:
        print(f"{severity} | {action} | risk={risk} => {remediate(severity, action, risk)}")

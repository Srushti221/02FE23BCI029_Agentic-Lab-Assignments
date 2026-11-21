"""Assignment 14A - Add password-reset guidance as a second reusable skill.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a genuine second skill (e.g. "password-reset guidance") with its own instructions and constraints, alongside the existing `triage_skill`. Extend the node graph so the triage stage correctly routes between the two skills based on the issue text, and demonstrate both skills firing correctly on different inputs.
"""
FAQ = {"wifi": "Connect to Campus-Secure and sign in with your student ID."}
TICKETS = []

def triage_skill(issue):
    """General help-desk skill: check FAQ, otherwise create a support ticket.
    Constraint: do not invent an FAQ answer.
    """
    for keyword, answer in FAQ.items():
        if keyword in issue.lower(): return {"skill": "triage_skill", "route": "faq", "response": answer}
    ticket_id = f"T-{len(TICKETS) + 1:03d}"
    TICKETS.append({"id": ticket_id, "issue": issue, "status": "open"})
    return {"skill": "triage_skill", "route": "ticket", "response": f"Ticket {ticket_id} created."}

def password_reset_skill(issue):
    """Password guidance skill.
    Instructions: use the official reset page and verify identity.
    Constraints: never request the current password; never bypass verification.
    """
    return {"skill": "password_reset_guidance", "route": "verified_reset_steps",
            "steps": ["Open the official university password-reset page.",
                      "Complete the approved identity-verification process.",
                      "Choose a new, unique password."],
            "constraints": ["Do not share your current password.", "Do not bypass identity verification."]}

def route_node_graph(issue):
    text = issue.lower()
    if "password" in text or "forgot login" in text:
        selected = password_reset_skill(issue)
    else:
        selected = triage_skill(issue)
    return {"graph": ["intake", "triage_router", selected["skill"], "response"], "result": selected}

if __name__ == "__main__":
    for issue in ["I forgot my password and cannot log in", "How do I connect to campus wifi?"]:
        print("Issue:", issue)
        print("Execution:", route_node_graph(issue))

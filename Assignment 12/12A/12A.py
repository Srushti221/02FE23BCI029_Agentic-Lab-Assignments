"""Assignment 12A - Cost category and finance approval control.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a cost estimate to each proposed action and a budget threshold. Reject any proposal whose estimated cost exceeds the threshold unless a separate `finance_approved` flag is set. Write an adversarial test that attempts to bypass this by omitting the cost estimate entirely, and confirm it is rejected rather than defaulting to approved.
"""
BUDGET_THRESHOLD = 1000

def evaluate_proposal(action):
    if "cost" not in action or action["cost"] is None:
        return {"approved": False, "reason": "cost estimate is missing; proposal rejected"}
    if not isinstance(action["cost"], (int, float)) or action["cost"] < 0:
        return {"approved": False, "reason": "cost must be a non-negative number"}
    if action["cost"] > BUDGET_THRESHOLD and action.get("finance_approved") is not True:
        return {"approved": False, "reason": "cost exceeds threshold and finance approval is absent"}
    return {"approved": True, "reason": "within threshold or separately finance-approved"}

if __name__ == "__main__":
    proposals = [
        {"name": "documentation update", "cost": 250},
        {"name": "large infrastructure change", "cost": 1500},
        {"name": "approved infrastructure change", "cost": 1500, "finance_approved": True},
        {"name": "adversarial missing-cost proposal"},
    ]
    for proposal in proposals:
        print(proposal["name"], "=>", evaluate_proposal(proposal))
    print("\nMissing-cost adversarial case rejected:", evaluate_proposal(proposals[-1])["approved"] is False)

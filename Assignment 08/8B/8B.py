"""Assignment 8B - Distributed critique by independent swarm roles.
Name: Srushti Bandi | SRN: 02FE23BCI029
Assignment question: Replace the single central `critique()` function with a design where each of the four (or five) roles critiques the merged draft independently against its own constraints, and the conflict log records which specific role raised each objection. Submit the updated code and a transcript showing at least two different roles independently raising objections. 
"""
merged_draft = {
    "venue": "Grand Hall", "venue_available": False, "venue_cost": 45000,
    "budget_cap": 30000, "marketing_cost": 36000,
    "date": "Saturday", "judging_criteria": ["innovation", "technical depth"],
}

def research_agent_critique(draft):
    return None if draft["date"] == "Saturday" else "Date differs from the preferred Saturday event format."
def logistics_agent_critique(draft):
    return None if draft["venue_available"] else f"Venue {draft['venue']} is not available."
def budget_agent_critique(draft):
    total = draft["venue_cost"] + draft["marketing_cost"]
    return None if total <= draft["budget_cap"] else f"Combined cost {total} exceeds cap {draft['budget_cap']}."
def judging_agent_critique(draft):
    required = {"innovation", "technical depth", "demo quality"}
    missing = required - set(draft["judging_criteria"])
    return None if not missing else f"Judging criteria are missing: {sorted(missing)}."
def marketing_agent_critique(draft):
    return None if draft["marketing_cost"] <= draft["budget_cap"] else "Publicity proposal exceeds the available budget cap."

ROLE_REVIEWS = {
    "research_agent": research_agent_critique,
    "logistics_agent": logistics_agent_critique,
    "budget_agent": budget_agent_critique,
    "judging_agent": judging_agent_critique,
    "marketing_agent": marketing_agent_critique,
}

def distributed_critique(draft):
    conflict_log = []
    for role_name, reviewer in ROLE_REVIEWS.items():
        objection = reviewer(draft)
        if objection:
            conflict_log.append({"role": role_name, "objection": objection})
    return conflict_log

if __name__ == "__main__":
    print("Merged draft:", merged_draft)
    print("\nIndependent role critiques:")
    log = distributed_critique(merged_draft)
    for item in log: print(item)
    roles_raising_objections = sorted({item["role"] for item in log})
    print("\nDistinct roles raising objections:", roles_raising_objections)
    print("At least two independent roles raised objections:", len(roles_raising_objections) >= 2)

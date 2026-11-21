"""Assignment 8A - Add a fifth marketing role to the parallel swarm.
Name: Srushti Bandi | SRN: 02FE23BCI029
Assignment question: Add a `marketing_agent` role proposing a publicity plan with its own cost. Extend `critique()` to detect a new conflict between the marketing budget and the same overall budget cap, and resolve it with the same `budget_over_preference` rule. Submit the updated code and the extended conflict log. 
"""
from concurrent.futures import ThreadPoolExecutor

def research_agent(goal):
    return {"role": "research", "output": "Past events favored a 24-hour format with themed tracks."}
def logistics_agent(goal):
    return {"role": "logistics", "output": {"venue": "Grand Hall", "venue_cost": 45000, "date": "Saturday"}}
def budget_agent(goal):
    return {"role": "budget", "output": {"total_cap": 30000}}
def judging_agent(goal):
    return {"role": "judging", "output": "Judge on innovation, technical depth, and demo quality."}
def marketing_agent(goal):
    return {"role": "marketing", "output": {"publicity_plan": "Campus social-media and poster campaign", "marketing_cost": 36000}}

ROLES = {"research": research_agent, "logistics": logistics_agent, "budget": budget_agent,
         "judging": judging_agent, "marketing": marketing_agent}

def run_swarm(goal):
    with ThreadPoolExecutor(max_workers=len(ROLES)) as pool:
        futures = {name: pool.submit(function, goal) for name, function in ROLES.items()}
        return {name: future.result() for name, future in futures.items()}

def merge(outputs):
    return {"format_notes": outputs["research"]["output"],
            "venue": outputs["logistics"]["output"]["venue"],
            "venue_cost": outputs["logistics"]["output"]["venue_cost"],
            "date": outputs["logistics"]["output"]["date"],
            "budget_cap": outputs["budget"]["output"]["total_cap"],
            "judging_criteria": outputs["judging"]["output"],
            "publicity_plan": outputs["marketing"]["output"]["publicity_plan"],
            "marketing_cost": outputs["marketing"]["output"]["marketing_cost"]}

def critique(draft):
    conflicts = []
    if draft["venue_cost"] > draft["budget_cap"]:
        conflicts.append({"conflict": "venue_cost exceeds budget_cap", "roles_involved": ["logistics", "budget"],
                          "proposed_value": draft["venue_cost"], "budget_cap": draft["budget_cap"]})
    if draft["marketing_cost"] > draft["budget_cap"]:
        conflicts.append({"conflict": "marketing_cost exceeds budget_cap", "roles_involved": ["marketing", "budget"],
                          "proposed_value": draft["marketing_cost"], "budget_cap": draft["budget_cap"]})
    return conflicts

def resolve(conflict, priority_rule="budget_over_preference"):
    if conflict["conflict"] == "venue_cost exceeds budget_cap":
        message = f"Reject the {conflict['proposed_value']} venue; ask logistics for an alternative under {conflict['budget_cap']}."
    elif conflict["conflict"] == "marketing_cost exceeds budget_cap":
        message = f"Reduce the publicity plan from {conflict['proposed_value']} to no more than {conflict['budget_cap']}."
    else:
        message = "No matching resolution rule."
    return {"rule_applied": priority_rule, "resolution": message}

if __name__ == "__main__":
    outputs = run_swarm("Plan a college AI hackathon")
    print("=== Parallel role outputs ===")
    for name, output in outputs.items(): print(f"{name}: {output['output']}")
    draft = merge(outputs)
    print("\n=== Merged draft ===")
    print(draft)
    conflicts = critique(draft)
    print("\n=== Extended conflict log ===")
    conflict_log = []
    for conflict in conflicts:
        entry = {**conflict, **resolve(conflict)}
        conflict_log.append(entry)
        print(entry)
    print("\nMarketing conflict detected:", any(x["conflict"] == "marketing_cost exceeds budget_cap" for x in conflict_log))
    print("Resolution rule used:", all(x["rule_applied"] == "budget_over_preference" for x in conflict_log))

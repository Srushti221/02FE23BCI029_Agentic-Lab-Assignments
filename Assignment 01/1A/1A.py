"""
Subject: Agentic AI Systems
Lab: 1 - Agent vs Chatbot
Assignment: 1A
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Extend the reference agent to accept a second, independent round of feedback after the first revision (e.g. "also make Friday's session shorter, only one hour"). Both revisions must mutate the same plan object — the log must show two separate revise iterations, neither of which regenerates the plan from scratch. Submit the updated code and the full iteration log covering both rounds.
"""

import json
plan = {"Monday":{"subject":"Data Structures","hours":2},"Tuesday":{"subject":"Operating Systems","hours":2},"Wednesday":{"subject":"AI Agents","hours":2},"Thursday":{"subject":"Data Structures","hours":2},"Friday":{"subject":"Operating Systems","hours":2}}
log=[]
def revise(feedback):
    # Mutate the existing plan; do not rebuild it.
    if "tuesday" in feedback.lower() and "evening" in feedback.lower(): plan["Tuesday"]["time"]="20:00-22:00"
    if "friday" in feedback.lower() and "one hour" in feedback.lower(): plan["Friday"]["hours"]=1
    log.append({"revision":len(log)+1,"feedback":feedback,"plan_id":id(plan)})
revise("Move Tuesday's session to the evening.")
revise("Also make Friday's session shorter, only one hour.")
print("=== Revised study plan ===")
print(json.dumps(plan,indent=2))
print("=== Revision log ===")
for item in log: print(item)
print("Same plan object used for both revisions:",len({x['plan_id'] for x in log})==1)

"""
Subject: Agentic AI Systems
Lab: 1 - Agent vs Chatbot
Assignment: 1B
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Extend `read_existing_schedule` to return a second busy day, then modify `_build_plan` (or add a check before it) so that if the student's chosen unavailable days do not actually avoid every busy day returned by the tool, the agent flags the conflict explicitly to the user before finalizing the plan, rather than silently double-booking. Submit the updated code and a transcript showing the conflict being detected and reported.
"""

busy_days={"Wednesday","Friday"}
unavailable_days={"Sunday"}
conflicts=sorted(busy_days-unavailable_days)
print("Busy days returned by schedule tool:",sorted(busy_days))
print("Student unavailable days:",sorted(unavailable_days))
if conflicts:
    print("SCHEDULING CONFLICT DETECTED:",", ".join(conflicts))
    print("Plan was not finalized. Please choose different study days or update availability.")
else:
    print("No conflicts found. Plan can be finalized.")

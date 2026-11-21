"""
Subject: Agentic AI Systems
Lab: 2 - Tool-Using Agent
Assignment: 2B
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Add a category field to the CSV data (e.g. "technical" vs "social") and implement a new question ("What's the average sign-up for technical events only?") that requires three steps: read the CSV, filter rows by category, then compute the average over the filtered subset. Validate the filter step's output (non-empty) before computing the average. Submit the updated code and the trace for this new question.
"""

import csv,io
DATA="""event,signups,category
AI Club Talk,12,technical
Hackathon Kickoff,9,technical
Robotics Demo,15,technical
Cultural Fest,20,social
Career Panel,11,social
"""
rows=list(csv.DictReader(io.StringIO(DATA)))
print("Question: What's the average sign-up for technical events only?")
print("Tool 1 - read_csv: rows read =",len(rows))
filtered=[r for r in rows if r["category"]=="technical"]
print("Tool 2 - filter category=technical:",[(r["event"],int(r["signups"])) for r in filtered])
if not filtered: raise ValueError("No technical events found; average cannot be calculated.")
values=[int(r["signups"]) for r in filtered]
avg=sum(values)/len(values)
print("Tool 3 - calculator input:",values)
print(f"Average technical-event sign-ups: {avg:.2f}")
print("Trace validation: filtered subset is non-empty.")

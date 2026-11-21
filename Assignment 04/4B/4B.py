"""
Subject: Agentic AI Systems
Lab: 4 - Memory and Retrieval
Assignment: 4B
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Add a `retention_days` control and a staleness check: if a retrieved record is older than the configured threshold, the assistant must warn the user ("this decision is from N days ago and may be out of date") before using it in an answer. Test it with one fresh record and one artificially old record. Submit the updated code and a transcript showing both cases.
"""

from datetime import date
retention_days=30
today=date(2026,11,20)
records=[("fresh decision","Use SQLite.",date(2026,11,10)),("old decision","Use PostgreSQL.",date(2026,9,1))]
for topic,fact,stored in records:
    age=(today-stored).days
    print(f"Topic: {topic} | Fact: {fact} | Stored: {stored} | Age: {age} days")
    if age>retention_days:
        print(f"WARNING: this decision is from {age} days ago and may be out of date.")
    else:
        print("Fresh record: safe to use within retention period.")

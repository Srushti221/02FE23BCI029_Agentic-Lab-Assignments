"""
Subject: Agentic AI Systems
Lab: 4 - Memory and Retrieval
Assignment: 4A
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Add a second topic (e.g. "hosting") with its own stored record, distinct from "database". Demonstrate, in a transcript, that a retrieval scoped to "database" never returns or leaks the "hosting" fact into its answer, and vice versa. Submit the updated code and the two-topic transcript.
"""

from dataclasses import dataclass
@dataclass
class MemoryRecord: topic:str; fact:str; date:str
records=[MemoryRecord("database","We chose PostgreSQL.","2026-07-03"),MemoryRecord("hosting","The application will use AWS.","2026-07-04")]
def retrieve(topic): return [r for r in records if r.topic==topic]
for topic in ("database","hosting"):
    result=retrieve(topic)
    print(f"Retrieval for {topic}:")
    for r in result: print(f" [{r.topic}] {r.fact}")
    assert all(r.topic==topic for r in result)
print("Isolation check: PASS - database and hosting records do not leak across topics.")

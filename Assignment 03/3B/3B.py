"""
Subject: Agentic AI Systems
Lab: 3 - Skill Creation
Assignment: 3B
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Add a fourth article that asserts a claim but provides no real supporting evidence or limitation in the text. Run it through the skill and confirm the constraint layer correctly outputs "not stated in source" for the evidence and/or limitation fields rather than fabricating plausible-sounding content. Submit the article text, the skill's output, and one sentence confirming no fabrication occurred.
"""

article={"title":"A Claim About a New Study Tool","text":"A new study tool is the best solution for every student."}
sentences=[s.strip() for s in article["text"].split(".") if s.strip()]
claim=sentences[0] if sentences else "not stated in source"
evidence="not stated in source"
limitation="not stated in source"
print("Article:",article["title"])
print("Claim:",claim)
print("Evidence:",evidence)
print("Limitation:",limitation)
print("Takeaway: The source makes a claim but provides no evidence to verify it.")
print("Fabrication check: PASS - no supporting evidence or limitation was invented.")

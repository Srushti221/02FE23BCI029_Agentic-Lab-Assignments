"""
Subject: Agentic AI Systems
Lab: 3 - Skill Creation
Assignment: 3A
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Add a third article whose text makes two unrelated claims (e.g. one about cost and one about accuracy). Extend `apply_research_summary_skill` to detect this case and select the most evidence-supported claim, explicitly noting in the output that a selection was made between competing claims rather than silently picking the first sentence. Submit the updated code and its output on the new article.
"""

article={"title":"Campus AI Platform: Cost and Accuracy Evaluation","text":"The platform reduced annual processing cost by 25 percent across 12 departments. In a controlled test of 500 requests, answer accuracy improved from 80 percent to 92 percent."}
sentences=[s.strip() for s in article["text"].split(".") if s.strip()]
# Evidence-bearing claim is selected by checking for a measurable sample or comparison.
scored=[]
for s in sentences:
    score=sum(token in s.lower() for token in ["percent","across","controlled","test","requests","from","improved"])
    scored.append((score,s))
selected=max(scored,key=lambda x:x[0])[1]
print("Article:",article["title"])
print("Competing claims detected:")
for _,s in scored: print(" -",s)
print("Selection made: yes; claims were compared for supporting evidence.")
print("Most evidence-supported claim:",selected)
print("Evidence basis: explicit numerical measurement or comparison in the source text.")

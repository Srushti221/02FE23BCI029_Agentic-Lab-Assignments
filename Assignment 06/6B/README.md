# Assignment 6B: Escalate After Two Failures

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 6 - OpenCLA/OpenClaw Runtime

## Question
Add a rule: if the same skill fails twice in one session for the same user, the third attempt must escalate to a human instead of retrying the skill again. Implement this using the existing audit log (count prior error entries for that user/skill pair) rather than adding new hidden state. Submit the updated code and a transcript showing two failures followed by an escalation instead of a third attempt.

## Files
- `6B.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 6B.py
```

The program uses deterministic sample data and does not require API keys or external services.

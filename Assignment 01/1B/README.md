# Assignment 1B: Detect a Scheduling Conflict

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 1 - Agent vs Chatbot

## Question
Extend `read_existing_schedule` to return a second busy day, then modify `_build_plan` (or add a check before it) so that if the student's chosen unavailable days do not actually avoid every busy day returned by the tool, the agent flags the conflict explicitly to the user before finalizing the plan, rather than silently double-booking. Submit the updated code and a transcript showing the conflict being detected and reported.

## Files
- `1B.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 1B.py
```

The program uses deterministic sample data and does not require API keys or external services.

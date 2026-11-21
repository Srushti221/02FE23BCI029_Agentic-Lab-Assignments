# Assignment 6A: Add Per-User Rate Limiting

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 6 - OpenCLA/OpenClaw Runtime

## Question
Add a new control: each user may run at most 3 tasks per session. Implement this as a check inside `receive_task` (or a thin wrapper around it) without changing `run_task`'s core loop signature or its skill-dispatch logic. Submit the updated code and a transcript showing a 4th task being rejected.

## Files
- `6A.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 6A.py
```

The program uses deterministic sample data and does not require API keys or external services.

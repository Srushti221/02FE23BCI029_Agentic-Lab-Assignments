# Assignment 10B: A Safe Auto-Remediation Path

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 10 - Cloud Operations Agent

## Question
Add a WARNING-level (not ALARM/degraded-critical) scenario where the proposed action is a low-risk `restart_single_pod`. Demonstrate that this low-risk action is allowed to execute automatically (per `risk_level`), while any rollback-class action anywhere in your extended code still always routes through the approval-request path and never auto-executes.

## Files
- `10B.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 10B.py
```

The program uses deterministic sample data and does not require API keys or external services.

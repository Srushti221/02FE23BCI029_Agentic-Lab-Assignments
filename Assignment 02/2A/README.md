# Assignment 2A: Add a Notification Tool with Justified Use

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 2 - Tool-Using Agent

## Question
Add a fourth tool, `send_notification(message)`, that only drafts a message (it must not actually send anything). Extend the assistant so that when the computed average sign-ups falls below a threshold you define (e.g. 10), it calls this tool to draft a low-turnout notice, and states in the trace why the tool was needed. Submit the updated code and a transcript showing the notification being drafted with its justification.

## Files
- `2A.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 2A.py
```

The program uses deterministic sample data and does not require API keys or external services.

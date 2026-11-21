# Assignment 4B: A Staleness / Retention Policy

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 4 - Memory and Retrieval

## Question
Add a `retention_days` control and a staleness check: if a retrieved record is older than the configured threshold, the assistant must warn the user ("this decision is from N days ago and may be out of date") before using it in an answer. Test it with one fresh record and one artificially old record. Submit the updated code and a transcript showing both cases.

## Files
- `4B.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 4B.py
```

The program uses deterministic sample data and does not require API keys or external services.

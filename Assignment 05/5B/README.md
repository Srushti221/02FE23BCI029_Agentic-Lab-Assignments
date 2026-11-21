# Assignment 5B: Scope read_file to a Safe Directory

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 5 - MCP-Style Connector

## Question
Add a second permission boundary: `read_file` may only read paths inside a declared safe directory (e.g. paths starting with `/safe/`). Write an adversarial test that attempts to read a path outside that directory and confirm the server rejects it with a structured error rather than reading it. Submit the updated code and the adversarial test's result.

## Files
- `5B.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 5B.py
```

The program uses deterministic sample data and does not require API keys or external services.

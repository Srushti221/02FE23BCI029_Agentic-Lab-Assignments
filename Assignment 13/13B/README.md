# Assignment 13B: Escalate on a Trend, Not Just a Threshold

**Subject:** Agentic AI Systems  
**Name:** Srushti Bandi  
**SRN:** 02FE23BCI029  
**Lab:** 13 - Discipline-Specific Engineering Agents

## Question
Extend the Mechanical agent so that three consecutive WARNING-level readings (even if none individually reaches ALARM) escalate to a "schedule_inspection" recommendation instead of "continue_monitoring". Demonstrate this with a modified sensor log that stays under the ALARM threshold throughout but trends upward for three readings.

## Files
- `13B.py` — complete standalone Python implementation.
- `output.txt` — actual console output captured by executing the Python file.

## Run
```bash
python 13B.py
```

The program uses deterministic sample data and does not require API keys or external services.

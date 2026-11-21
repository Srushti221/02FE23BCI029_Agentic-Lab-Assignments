"""Assignment 13A - Electrical load forecasting agent with human-review gate.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Implement a parallel agent for the Electrical Engineering example (load forecasting or fault-triage from sensor/power-consumption data), using a comparable threshold-based classification approach. Confirm the same human-review safety gate applies before any ALARM-equivalent recommendation is acted on.
"""
READINGS = [
    {"time": "10:00", "load_kw": 42, "voltage_v": 230},
    {"time": "10:15", "load_kw": 58, "voltage_v": 229},
    {"time": "10:30", "load_kw": 78, "voltage_v": 228},
]
WARNING_KW = 55
ALARM_KW = 75

def electrical_load_agent(reading):
    load = reading["load_kw"]
    if load >= ALARM_KW:
        return {"level": "ALARM", "recommendation": "inspect feeder and verify load source", "requires_human_review": True}
    if load >= WARNING_KW:
        return {"level": "WARNING", "recommendation": "monitor load and notify operator", "requires_human_review": False}
    return {"level": "NORMAL", "recommendation": "continue monitoring", "requires_human_review": False}

if __name__ == "__main__":
    for reading in READINGS:
        result = electrical_load_agent(reading)
        print(f"{reading['time']} | load={reading['load_kw']} kW | voltage={reading['voltage_v']} V => {result}")
        if result["level"] == "ALARM":
            print("Safety gate: recommendation is pending human review; no automatic action taken.")

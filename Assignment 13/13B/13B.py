"""Assignment 13B - Escalate after three consecutive WARNING readings.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Extend the Mechanical agent so that three consecutive WARNING-level readings (even if none individually reaches ALARM) escalate to a "schedule_inspection" recommendation instead of "continue_monitoring". Demonstrate this with a modified sensor log that stays under the ALARM threshold throughout but trends upward for three readings.
"""
READINGS = [48, 55, 61, 68, 72]  # rising values; all remain below ALARM=90
WARNING_THRESHOLD = 50
ALARM_THRESHOLD = 90

def analyze_sensor_log(readings):
    consecutive_warnings = 0
    recommendation = "continue_monitoring"
    for index, value in enumerate(readings, 1):
        if value >= ALARM_THRESHOLD:
            level = "ALARM"
            consecutive_warnings = 0
            recommendation = "urgent_human_review"
        elif value >= WARNING_THRESHOLD:
            level = "WARNING"
            consecutive_warnings += 1
        else:
            level = "NORMAL"
            consecutive_warnings = 0
        print(f"Reading {index}: vibration={value} -> {level}; consecutive warnings={consecutive_warnings}")
        if consecutive_warnings >= 3:
            recommendation = "schedule_inspection"
    return recommendation

if __name__ == "__main__":
    final_recommendation = analyze_sensor_log(READINGS)
    print("Final recommendation:", final_recommendation)
    print("Any ALARM reading:", any(value >= ALARM_THRESHOLD for value in READINGS))

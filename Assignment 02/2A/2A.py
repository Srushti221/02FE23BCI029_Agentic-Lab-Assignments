"""
Subject: Agentic AI Systems
Lab: 2 - Tool-Using Agent
Assignment: 2A
Name: Srushti Bandi
SRN: 02FE23BCI029

Assignment question:
Add a fourth tool, `send_notification(message)`, that only drafts a message (it must not actually send anything). Extend the assistant so that when the computed average sign-ups falls below a threshold you define (e.g. 10), it calls this tool to draft a low-turnout notice, and states in the trace why the tool was needed. Submit the updated code and a transcript showing the notification being drafted with its justification.
"""

events=[{"event":"AI Club Talk","signups":12},{"event":"Hackathon Kickoff","signups":9},{"event":"Robotics Demo","signups":7},{"event":"GenAI Workshop","signups":5}]
trace=[]
def calculator(values): return sum(values)/len(values)
def send_notification(message):
    # Draft only: no message is sent.
    return {"status":"drafted","message":message}
values=[e["signups"] for e in events]
avg=calculator(values)
trace.append({"tool":"calculator","reason":"calculate average event sign-ups","input":values,"output":avg})
print(f"Average sign-ups: {avg:.2f}")
if avg < 10:
    message=f"Low turnout notice: average sign-ups are {avg:.2f}, below the threshold of 10. Please promote upcoming events."
    result=send_notification(message)
    trace.append({"tool":"send_notification","reason":"average is below the low-turnout threshold","input":message,"output":result})
    print("Notification draft:",result["message"])
    print("Notification sent: No (draft only)")
print("=== Tool trace ===")
for row in trace: print(row)

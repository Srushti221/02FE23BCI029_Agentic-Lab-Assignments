"""Assignment 7B - Builder gets exactly one retry.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Modify the graph so the `builder` node is allowed exactly one retry before escalating to a human. Implement and demonstrate two scenarios: (a) the builder fails once, retries, and succeeds; (b) the builder fails twice and correctly escalates instead of retrying a third time.
"""

def run_builder(fail_attempts):
    max_attempts = 2  # initial attempt + exactly one retry
    for attempt in range(1, max_attempts + 1):
        print(f"Builder attempt {attempt}")
        if attempt > fail_attempts:
            print("Builder result: SUCCESS")
            return "success"
        print("Builder result: FAILED")
        if attempt < max_attempts:
            print("Retrying once (one retry is permitted).")
    print("Retry limit reached. Escalating to human; no third attempt.")
    return "escalated"

if __name__ == "__main__":
    print("=== Scenario A: first attempt fails, retry succeeds ===")
    result_a = run_builder(fail_attempts=1)
    print("Final status:", result_a)
    print("\n=== Scenario B: both allowed attempts fail ===")
    result_b = run_builder(fail_attempts=2)
    print("Final status:", result_b)

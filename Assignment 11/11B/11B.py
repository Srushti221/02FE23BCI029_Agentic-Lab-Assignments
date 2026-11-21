"""Assignment 11B - Independent tests catch a deliberate coding bug.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Introduce a deliberate bug into `coding_agent`'s filter logic (e.g. an off-by-one or inverted comparison) without changing `testing_agent`. Run the pipeline and confirm the independently-generated tests catch the regression — submit the failing test output as evidence that the tests were not simply validating whatever the code happened to do.
"""
RECORDS = [{"name": "Ada", "score": 70}, {"name": "Ben", "score": 85}, {"name": "Cara", "score": 60}]

# Deliberate bug introduced only in coding_agent: > should have been >=.
def coding_agent(data):
    return [record for record in data if record["score"] > 70]

# Independent acceptance test: tests the stated requirement, not the code's implementation.
def testing_agent(actual_records):
    expected_names = ["Ada", "Ben"]  # requirement: score >= 70
    actual_names = [record["name"] for record in actual_records]
    print("Expected records:", expected_names)
    print("Actual records:", actual_names)
    if actual_names != expected_names:
        print("FAIL: boundary case score=70 was excluded by the buggy filter.")
        return False
    print("PASS")
    return True

if __name__ == "__main__":
    print("=== Coding agent output (deliberate defect present) ===")
    output = coding_agent(RECORDS)
    print(output)
    print("\n=== Independently generated test result ===")
    passed = testing_agent(output)
    print("Regression detected:", not passed)

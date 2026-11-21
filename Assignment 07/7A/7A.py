"""Assignment 7A - Insert a security_scan node in the graph.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Insert a new `security_scan` node between `builder` and `tester`, with its own input, output, owner, success criteria, and failure behavior. Update both the success-path and failure-path simulations to include it, and produce a case where the security scan itself is the node that fails.
"""
NODES = ["planner", "builder", "security_scan", "tester", "reviewer"]
NODE_CONTRACTS = {
    "security_scan": {
        "input": "built application", "output": "security findings",
        "owner": "security agent", "success_criteria": "no high-severity findings",
        "failure_behavior": "stop pipeline and request human review",
    }
}

def run_pipeline(fail_node=None):
    print("Graph:", " -> ".join(NODES))
    for node in NODES:
        print(f"Running node: {node}")
        if node == "security_scan":
            print("Security scan input: built application")
            print("Security scan output: no high-severity findings" if fail_node != node else "Security scan output: high-severity vulnerability")
        if node == fail_node:
            print(f"Node failure: {node}")
            print(NODE_CONTRACTS["security_scan"]["failure_behavior"] if node == "security_scan" else "Pipeline stopped due to node failure.")
            return False
    print("Pipeline status: SUCCESS")
    return True

if __name__ == "__main__":
    print("=== Security scan node contract ===")
    for key, value in NODE_CONTRACTS["security_scan"].items(): print(f"{key}: {value}")
    print("\n=== Success path ===")
    run_pipeline()
    print("\n=== Security scan failure path ===")
    run_pipeline(fail_node="security_scan")

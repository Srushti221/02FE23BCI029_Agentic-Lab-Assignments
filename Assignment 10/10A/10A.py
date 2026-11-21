"""Assignment 10A - Add a database connection-pool exhaustion incident.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a second scenario: a database connection-pool exhaustion incident, with its own log lines, deploy history, and metrics. Confirm `classify_severity` and `correlate_with_recent_changes` correctly produce a different diagnosis and severity than the reference payments-service scenario.
"""
SCENARIOS = [
    {"service": "payments", "logs": ["HTTP 500 rate increased", "payment gateway timeout"],
     "deploy_history": ["payments-v2.4 deployed 10 minutes before alert"],
     "metrics": {"error_rate_pct": 4.5, "latency_ms": 1800}},
    {"service": "database", "logs": ["connection pool exhausted", "requests waiting for connection"],
     "deploy_history": ["reporting-v1.8 deployed 8 minutes before alert"],
     "metrics": {"pool_usage_pct": 100, "waiting_connections": 42}},
]

def classify_severity(incident):
    metrics = incident["metrics"]
    if metrics.get("error_rate_pct", 0) >= 7 or metrics.get("pool_usage_pct", 0) >= 95:
        return "ALARM"
    return "WARNING"

def correlate_with_recent_changes(incident):
    if incident["service"] == "database" and incident["metrics"].get("pool_usage_pct", 0) >= 95:
        return "Database connection-pool exhaustion; correlate with the recent reporting job deployment."
    if incident["service"] == "payments" and any("payment gateway timeout" in line.lower() for line in incident["logs"]):
        return "Payment gateway timeouts began after payments-v2.4; investigate the recent deployment."
    return "No clear recent-change correlation found."

if __name__ == "__main__":
    for incident in SCENARIOS:
        print("=== Incident:", incident["service"], "===")
        print("Logs:", incident["logs"])
        print("Deploy history:", incident["deploy_history"])
        print("Metrics:", incident["metrics"])
        print("Severity:", classify_severity(incident))
        print("Diagnosis:", correlate_with_recent_changes(incident))

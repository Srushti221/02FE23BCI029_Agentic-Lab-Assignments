import sqlite3


"""Assignment 5A - Add a discoverable list_files resource.
Name: Srushti Bandi | SRN: 02FE23BCI029
Assignment question: Add a `list_files` resource capability to the manifest and server. The client must discover and call it without any hard-coded reference to its name anywhere in `MCPClient` — only `CAPABILITIES` should need to change. Submit the updated server/client code and a transcript demonstrating the new capability being discovered and called.
"""

MOCK_FILES = {
    "/safe/README.md": "Mini MCP server demonstration.",
    "/safe/events.txt": "AI Club Talk\nRobotics Demo",
}

# The manifest is the discovery source. Adding a capability requires a
# server method and a manifest entry, not a new branch in MCPClient.call.
CAPABILITIES = [
    {"name": "read_file", "kind": "resource", "input": {"path": "str"}, "output": {"content": "str"}},
    {"name": "query_db", "kind": "tool", "input": {"sql": "str"}, "output": {"rows": "list"}},
    {"name": "call_api", "kind": "tool", "input": {"endpoint": "str"}, "output": {"data": "any"}},
    {"name": "list_files", "kind": "resource", "input": {}, "output": {"files": "list[str]"}},
]

class MCPServer:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute("CREATE TABLE signups (event TEXT, count INTEGER)")
        self.connection.executemany("INSERT INTO signups VALUES (?, ?)", [("AI Club Talk", 12), ("Robotics Demo", 15)])
        self.connection.commit()

    def list_capabilities(self):
        return CAPABILITIES

    def read_file(self, path):
        if path not in MOCK_FILES:
            return {"error": "not_found", "message": f"File not found: {path}"}
        return {"content": MOCK_FILES[path]}

    def query_db(self, sql, caller):
        if caller != "planning_agent":
            return {"error": "permission_denied", "message": "Caller is not permitted."}
        if not sql.strip().upper().startswith("SELECT"):
            return {"error": "invalid_query", "message": "Only SELECT statements are allowed."}
        try:
            return {"rows": self.connection.execute(sql).fetchall()}
        except sqlite3.Error as error:
            return {"error": "database_error", "message": str(error)}

    def call_api(self, endpoint):
        if endpoint != "events_today":
            return {"error": "not_found", "message": "Unknown API endpoint."}
        return {"data": ["AI Club Talk", "Robotics Demo"]}

    def list_files(self):
        return {"files": sorted(MOCK_FILES.keys())}

class MCPClient:
    def __init__(self, server, caller_name):
        self.server = server
        self.caller_name = caller_name

    def discover(self):
        return self.server.list_capabilities()

    def call(self, capability_name, **kwargs):
        manifest = {item["name"]: item for item in self.discover()}
        if capability_name not in manifest:
            return {"error": "unknown_capability", "message": capability_name}
        method = getattr(self.server, capability_name, None)
        if method is None:
            return {"error": "not_implemented", "message": capability_name}
        # Caller context is supplied to the database capability only.
        if capability_name == "query_db":
            return method(caller=self.caller_name, **kwargs)
        return method(**kwargs)

if __name__ == "__main__":
    client = MCPClient(MCPServer(), "planning_agent")
    print("=== Discovered capabilities ===")
    for capability in client.discover():
        print(f"{capability['name']} ({capability['kind']})")
    print("\n=== Call newly discovered list_files resource ===")
    print(client.call("list_files"))

import posixpath


"""Assignment 5B - Restrict read_file to a safe directory.
Name: Srushti Bandi | SRN: 02FE23BCI029
Assignment question: Add a second permission boundary: `read_file` may only read paths inside a declared safe directory (e.g. paths starting with `/safe/`). Write an adversarial test that attempts to read a path outside that directory and confirm the server rejects it with a structured error rather than reading it. Submit the updated code and the adversarial test's result.
"""
SAFE_DIRECTORY = "/safe"
FILES = {
    "/safe/notes.txt": "Agentic AI lab notes.",
    "/private/passwords.txt": "This file must never be exposed.",
}

def read_file(path):
    if not isinstance(path, str) or not path:
        return {"error": "invalid_path", "message": "A non-empty path is required."}
    normalized = posixpath.normpath(path)
    # Require a canonical absolute path strictly below /safe. This blocks
    # traversal such as /safe/../private/secrets.txt.
    if not normalized.startswith(SAFE_DIRECTORY + "/"):
        return {"error": "permission_denied", "message": "read_file is restricted to /safe/."}
    if normalized not in FILES:
        return {"error": "not_found", "message": "The requested file does not exist."}
    return {"content": FILES[normalized]}

if __name__ == "__main__":
    print("=== Allowed read ===")
    print(read_file("/safe/notes.txt"))
    print("\n=== Adversarial: outside safe directory ===")
    outside = read_file("/private/passwords.txt")
    print(outside)
    print("Rejected:", outside.get("error") == "permission_denied")
    print("\n=== Adversarial: path traversal ===")
    traversal = read_file("/safe/../private/passwords.txt")
    print(traversal)
    print("Traversal rejected:", traversal.get("error") == "permission_denied")

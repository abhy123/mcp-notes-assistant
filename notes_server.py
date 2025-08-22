# notes_server.py
import os
from mcp.server.fastmcp import FastMCP

# Initialize server
mcp = FastMCP("notes-server")

# Directory for notes
NOTES_DIR = "mcp_a/notes"
os.makedirs(NOTES_DIR, exist_ok=True)  # Ensure folder exists

@mcp.tool()
def list_notes():
    """List all available notes in the notes folder."""
    return {"notes": os.listdir(NOTES_DIR)}

@mcp.tool()
def read_note(filename: str):
    """Read the contents of a note."""
    path = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(path):
        return {"error": f"File {filename} not found"}
    with open(path, "r") as f:
        return {"content": f.read()}

@mcp.tool()
def search_notes(query: str):
    """Search for a keyword in all notes."""
    results = []
    for fname in os.listdir(NOTES_DIR):
        path = os.path.join(NOTES_DIR, fname)
        if not os.path.isfile(path):
            continue
        with open(path, "r") as f:
            content = f.read()
            if query.lower() in content.lower():
                results.append({
                    "file": fname,
                    "snippet": content[:200]
                })
    return {"results": results}

if __name__ == "__main__":
    # Run as stdio server
    mcp.run()

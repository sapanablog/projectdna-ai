import os
from pathlib import Path


def read_file(path: str) -> str:
    """Read the contents of a file."""
    if not os.path.exists(path):
        return f"File '{path}' not found."

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> str:
    """Write content to a file."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File written: {path}"


def search_files(pattern: str) -> list[str]:
    """Search files using glob."""
    return sorted(str(p) for p in Path(".").glob(pattern))


def delete_file(path: str) -> str:
    """Delete a file."""
    if os.path.exists(path):
        os.remove(path)
        return f"File deleted: {path}"

    return f"File not found: {path}"
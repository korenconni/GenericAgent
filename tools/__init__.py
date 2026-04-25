"""Tools package for GenericAgent.

This package provides built-in tools that the agent can use during execution.
Each tool module exposes a schema (for the LLM) and a handler function.
"""

from .web_search import schema as web_search_schema, handle as web_search_handle
from .browser_navigate import schema as browser_navigate_schema, handle as browser_navigate_handle
from .browser_read import schema as browser_read_schema, handle as browser_read_handle
from .run_python import schema as run_python_schema, handle as run_python_handle

# Registry maps tool names to their (schema, handler) pairs
TOOL_REGISTRY = {
    "web_search": {
        "schema": web_search_schema,
        "handler": web_search_handle,
    },
    "browser_navigate": {
        "schema": browser_navigate_schema,
        "handler": browser_navigate_handle,
    },
    "browser_read": {
        "schema": browser_read_schema,
        "handler": browser_read_handle,
    },
    "run_python": {
        "schema": run_python_schema,
        "handler": run_python_handle,
    },
}


def get_all_schemas() -> list[dict]:
    """Return a list of all tool schemas suitable for passing to the LLM."""
    return [entry["schema"] for entry in TOOL_REGISTRY.values()]


def get_handler(tool_name: str):
    """Look up and return the handler callable for a given tool name.

    Args:
        tool_name: The name of the tool as declared in its schema.

    Returns:
        The handler callable, or None if the tool is not registered.
    """
    entry = TOOL_REGISTRY.get(tool_name)
    if entry is None:
        return None
    return entry["handler"]


__all__ = [
    "TOOL_REGISTRY",
    "get_all_schemas",
    "get_handler",
]

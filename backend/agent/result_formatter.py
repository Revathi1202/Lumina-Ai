"""
Converts raw MCP tool outputs into UI-friendly data.

The UI should never receive raw JSON, Python objects,
or MCP TextContent objects.
"""

import json


def _extract_text(result):
    """
    Extract readable text from different MCP result types.
    """

    # List of MCP TextContent objects
    if isinstance(result, list):

        texts = []

        for item in result:

            if hasattr(item, "text"):
                texts.append(item.text)

            else:
                texts.append(str(item))

        return "\n".join(texts)

    # Single MCP TextContent
    if hasattr(result, "text"):
        return result.text

    # Dictionary
    if isinstance(result, dict):

        if "data" in result:
            return result["data"]

        return result

    return result


def format_result(tool_name, result):
    """
    Returns UI-friendly structured output.

    Always returns:

    {
        "type": "...",
        "content": ...
    }
    """

    data = _extract_text(result)

    # -----------------------------
    # Dictionary
    # -----------------------------

    if isinstance(data, dict):

        return {
            "type": "key_value",
            "content": data
        }

    # -----------------------------
    # List
    # -----------------------------

    if isinstance(data, list):

        return {
            "type": "list",
            "content": data
        }

    # -----------------------------
    # String
    # -----------------------------

    if isinstance(data, str):

        # Try parsing JSON string

        try:

            parsed = json.loads(data)

            if isinstance(parsed, dict):

                return {
                    "type": "key_value",
                    "content": parsed
                }

            if isinstance(parsed, list):

                return {
                    "type": "list",
                    "content": parsed
                }

        except Exception:
            pass

        return {
            "type": "text",
            "content": data.strip()
        }

    # -----------------------------
    # Fallback
    # -----------------------------

    return {
        "type": "text",
        "content": str(data)
    }
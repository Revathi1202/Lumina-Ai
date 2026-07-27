"""
UI metadata for MCP tools.

This file contains only presentation details.
The backend still uses the actual MCP tool names.
"""

TOOL_METADATA = {

    "default": {
        "title": "Tool Execution",
        "description": "Executing MCP tool.",
        "icon": "⚙️"
    },

    "get_weather": {
        "title": "Weather Lookup",
        "description": "Retrieving live weather information.",
        "icon": "🌤"
    },

    "get_coordinates": {
        "title": "Location Lookup",
        "description": "Finding the requested location.",
        "icon": "📍"
    },

    "draw_diagram": {
        "title": "Diagram Generator",
        "description": "Creating a visual diagram.",
        "icon": "📊"
    },

    "search_pdf": {
        "title": "Document Search",
        "description": "Searching the uploaded document.",
        "icon": "📄"
    },

    "search_web": {
        "title": "Web Search",
        "description": "Searching trusted online sources.",
        "icon": "🌐"
    },

    "calculator": {
        "title": "Calculator",
        "description": "Performing the requested calculation.",
        "icon": "🧮"
    },

    "database_query": {
        "title": "Database Lookup",
        "description": "Retrieving information from the database.",
        "icon": "🗄️"
    }
}


def get_tool_metadata(tool_name: str):
    """
    Returns UI metadata for a tool.

    Unknown tools automatically use the default metadata.
    """

    return TOOL_METADATA.get(
        tool_name,
        TOOL_METADATA["default"]
    )
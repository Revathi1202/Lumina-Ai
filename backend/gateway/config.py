import os
from dotenv import load_dotenv

load_dotenv()

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")
MCP_GATEWAY_TOKEN = os.getenv("MCP_GATEWAY_TOKEN")

print("Loaded MCP Token:", MCP_GATEWAY_TOKEN)

GATEWAY_HOST = os.getenv("GATEWAY_HOST", "127.0.0.1")
GATEWAY_PORT = int(os.getenv("GATEWAY_PORT", 8000))
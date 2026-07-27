from typing import Any
from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str
    thread_id: str


class ChatResponse(BaseModel):
    answer: str
    execution_trace: list[dict[str, Any]]
    tool_calls: list[dict[str, Any]]
    tool_outputs: list[Any]
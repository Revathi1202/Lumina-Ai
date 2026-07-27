from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    tool: str
    arguments: dict = Field(default_factory=dict)


class PlannerOutput(BaseModel):
    needs_tool: bool
    tools: list[ToolCall] = Field(default_factory=list)
    reason: str



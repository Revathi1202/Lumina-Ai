from typing import Annotated, Any
from typing_extensions import TypedDict
from operator import add


class AgentState(TypedDict):
    user_query: str

    plan: dict

    selected_tools: Annotated[list[str], add]

    tool_calls: Annotated[list[dict[str, Any]], add]

    tool_outputs: Annotated[list[Any], add]

    execution_trace: Annotated[list[dict[str, Any]], add]

    final_answer: str
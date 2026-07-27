from contextlib import asynccontextmanager

from fastapi import FastAPI

from mcp_manager.client import mcp_client
from mcp_manager.registry import mcp_registry

from agent.graph import graph
from models import ChatRequest, ChatResponse


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("🚀 Starting AI Agent Backend...")

    await mcp_client.connect()
    await mcp_registry.initialize()

    print("✅ MCP Connected")
    print("✅ Tool Registry Loaded")

    yield

    print("🛑 Shutting down...")

    await mcp_client.disconnect()


app = FastAPI(
    title="AI Agent Backend",
    version="1.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {
        "message": "AI Agent Backend Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    state = {
        "user_query": request.query,
        "plan": {},
        "selected_tools": [],
        "tool_calls": [],
        "tool_outputs": [],
        "execution_trace": [],
        "final_answer": "",
    }

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    result = await graph.ainvoke(
        state,
        config=config
    )
    print(result["execution_trace"])

    return ChatResponse(
        answer=result["final_answer"],
        execution_trace=result["execution_trace"],
        tool_calls=result["tool_calls"],
        tool_outputs=result["tool_outputs"],
    )




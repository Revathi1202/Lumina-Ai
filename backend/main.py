# from contextlib import asynccontextmanager

# from fastapi import FastAPI

# from mcp_manager.client import mcp_client
# from mcp_manager.registry import mcp_registry

# from agent.graph import graph
# from models import ChatRequest, ChatResponse


# @asynccontextmanager
# async def lifespan(app: FastAPI):

#     print("🚀 Starting AI Agent Backend...")

#     await mcp_client.connect()
#     await mcp_registry.initialize()

#     print("✅ MCP Connected")
#     print("✅ Tool Registry Loaded")

#     yield

#     print("🛑 Shutting down...")

#     await mcp_client.disconnect()


# app = FastAPI(
#     title="AI Agent Backend",
#     version="1.0",
#     lifespan=lifespan
# )


# @app.get("/")
# async def root():
#     return {
#         "message": "AI Agent Backend Running"
#     }


# @app.get("/health")
# async def health():
#     return {
#         "status": "healthy"
#     }


# @app.post("/chat", response_model=ChatResponse)
# async def chat(request: ChatRequest):

#     state = {
#         "user_query": request.query,
#         "plan": {},
#         "selected_tools": [],
#         "tool_calls": [],
#         "tool_outputs": [],
#         "execution_trace": [],
#         "final_answer": "",
#     }

#     config = {
#         "configurable": {
#             "thread_id": request.thread_id
#         }
#     }

#     result = await graph.ainvoke(
#         state,
#         config=config
#     )
#     print(result["execution_trace"])

#     return ChatResponse(
#         answer=result["final_answer"],
#         execution_trace=result["execution_trace"],
#         tool_calls=result["tool_calls"],
#         tool_outputs=result["tool_outputs"],
#     )



from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from mcp_manager.client import mcp_client
from mcp_manager.registry import mcp_registry

from agent.graph import graph
from models import ChatRequest, ChatResponse

from database.database import (
    init_db,
    create_chat,
    get_chat,
    get_all_chats,
    rename_chat,
    delete_chat,
    save_message,
    load_messages,
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("🚀 Starting AI Agent Backend...")

    init_db()

    await mcp_client.connect()
    await mcp_registry.initialize()

    print("✅ Database Initialized")
    print("✅ MCP Connected")
    print("✅ Tool Registry Loaded")

    yield

    print("🛑 Shutting down...")

    await mcp_client.disconnect()


app = FastAPI(
    title="AI Agent Backend",
    version="1.0",
    lifespan=lifespan,
)


# ---------------------------
# Existing APIs
# ---------------------------

@app.get("/")
async def root():
    return {"message": "AI Agent Backend Running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


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

    return ChatResponse(
        answer=result["final_answer"],
        execution_trace=result["execution_trace"],
        tool_calls=result["tool_calls"],
        tool_outputs=result["tool_outputs"],
    )


# ---------------------------
# Chat Models
# ---------------------------

class CreateChatRequest(BaseModel):
    title: str = "New Chat"


class RenameChatRequest(BaseModel):
    title: str


class MessageRequest(BaseModel):
    role: str
    content: str


# ---------------------------
# Chat History APIs
# ---------------------------

@app.get("/chats")
def list_chats():
    return get_all_chats()


@app.post("/chats")
def new_chat(request: CreateChatRequest):
    chat_id = create_chat(request.title)
    return get_chat(chat_id)


@app.get("/chats/{chat_id}")
def get_chat_messages(chat_id: int):

    chat = get_chat(chat_id)

    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    return {
        "chat": chat,
        "messages": load_messages(chat_id)
    }


@app.post("/chats/{chat_id}/messages")
def add_message(chat_id: int, request: MessageRequest):

    if get_chat(chat_id) is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    save_message(
        chat_id,
        request.role,
        request.content
    )

    return {"message": "Saved successfully"}


@app.patch("/chats/{chat_id}")
def update_chat(chat_id: int, request: RenameChatRequest):

    if get_chat(chat_id) is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    rename_chat(
        chat_id,
        request.title
    )

    return {"message": "Chat renamed"}


@app.delete("/chats/{chat_id}")
def remove_chat(chat_id: int):

    if get_chat(chat_id) is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    delete_chat(chat_id)

    return {"message": "Chat deleted"}
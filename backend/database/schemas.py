from datetime import datetime
from typing import List

from pydantic import BaseModel


# -----------------------------
# Message
# -----------------------------

class MessageResponse(BaseModel):
    id: int
    role: str
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True


# -----------------------------
# Conversation
# -----------------------------

class ConversationResponse(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ConversationDetail(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    messages: List[MessageResponse]

    class Config:
        from_attributes = True


# -----------------------------
# Requests
# -----------------------------

class RenameConversationRequest(BaseModel):
    title: str
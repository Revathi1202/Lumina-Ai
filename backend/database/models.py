from datetime import datetime
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    title = Column(
        String,
        nullable=False,
        default="New Chat"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan",
        order_by="Message.timestamp"
    )


class Message(Base):
    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    conversation_id = Column(
        String,
        ForeignKey("conversations.id"),
        nullable=False
    )

    role = Column(
        String,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )
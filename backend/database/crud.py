from sqlalchemy.orm import Session
from sqlalchemy import desc

from .models import Conversation, Message


# ----------------------------
# Conversation CRUD
# ----------------------------

def create_conversation(db: Session):

    conversation = Conversation(
        title="New Chat"
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_all_conversations(db: Session):

    return (
        db.query(Conversation)
        .order_by(desc(Conversation.updated_at))
        .all()
    )


def get_conversation(db: Session, conversation_id: str):

    return (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )


def rename_conversation(
    db: Session,
    conversation_id: str,
    title: str,
):

    conversation = get_conversation(db, conversation_id)

    if conversation is None:
        return None

    conversation.title = title

    db.commit()
    db.refresh(conversation)

    return conversation


def delete_conversation(
    db: Session,
    conversation_id: str,
):

    conversation = get_conversation(db, conversation_id)

    if conversation is None:
        return False

    db.delete(conversation)
    db.commit()

    return True


# ----------------------------
# Message CRUD
# ----------------------------

def add_message(
    db: Session,
    conversation_id: str,
    role: str,
    content: str,
):

    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content,
    )

    db.add(message)

    conversation = get_conversation(
        db,
        conversation_id,
    )

    if conversation:
        conversation.updated_at = message.timestamp

    db.commit()
    db.refresh(message)

    return message


def get_messages(
    db: Session,
    conversation_id: str,
):

    return (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.timestamp.asc())
        .all()
    )


# ----------------------------
# Auto Rename First Message
# ----------------------------

def update_title_from_first_message(
    db: Session,
    conversation_id: str,
):

    conversation = get_conversation(
        db,
        conversation_id,
    )

    if conversation is None:
        return

    if conversation.title != "New Chat":
        return

    first_message = (
        db.query(Message)
        .filter(
            Message.conversation_id == conversation_id,
            Message.role == "user",
        )
        .order_by(Message.timestamp.asc())
        .first()
    )

    if first_message:

        conversation.title = (
            first_message.content[:40]
            + ("..." if len(first_message.content) > 40 else "")
        )

        db.commit()
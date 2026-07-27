import sqlite3
from datetime import datetime

DB_NAME = "chat_history.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Chats table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        created_at TEXT
    )
    """)

    # Messages table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        role TEXT,
        content TEXT,
        timestamp TEXT,
        FOREIGN KEY(chat_id) REFERENCES chats(id)
    )
    """)

    conn.commit()
    conn.close()
    
    
from datetime import datetime


def create_chat(title="New Chat"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats (title, created_at)
        VALUES (?, ?)
        """,
        (title, datetime.now().isoformat())
    )

    chat_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return chat_id


def save_message(chat_id, role, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages (chat_id, role, content, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (chat_id, role, content, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()


def load_messages(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content
        FROM messages
        WHERE chat_id = ?
        ORDER BY id
        """,
        (chat_id,)
    )

    messages = cursor.fetchall()

    conn.close()

    return messages

def get_all_chats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title
        FROM chats
        ORDER BY id DESC
    """)

    chats = cursor.fetchall()

    conn.close()

    return chats

def rename_chat(chat_id, title):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET title = ?
        WHERE id = ?
        """,
        (title, chat_id),
    )

    conn.commit()
    conn.close()
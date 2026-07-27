# import sqlite3
# from datetime import datetime

# DB_NAME = "chat_history.db"


# def get_connection():
#     return sqlite3.connect(DB_NAME, check_same_thread=False)


# def init_db():
#     conn = get_connection()
#     cursor = conn.cursor()

#     # Chats table
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS chats (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT,
#         created_at TEXT
#     )
#     """)

#     # Messages table
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS messages (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         chat_id INTEGER,
#         role TEXT,
#         content TEXT,
#         timestamp TEXT,
#         FOREIGN KEY(chat_id) REFERENCES chats(id)
#     )
#     """)

#     conn.commit()
#     conn.close()
    
    
# from datetime import datetime


# def create_chat(title="New Chat"):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         """
#         INSERT INTO chats (title, created_at)
#         VALUES (?, ?)
#         """,
#         (title, datetime.now().isoformat())
#     )

#     chat_id = cursor.lastrowid

#     conn.commit()
#     conn.close()

#     return chat_id


# def save_message(chat_id, role, content):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         """
#         INSERT INTO messages (chat_id, role, content, timestamp)
#         VALUES (?, ?, ?, ?)
#         """,
#         (chat_id, role, content, datetime.now().isoformat())
#     )

#     conn.commit()
#     conn.close()


# def load_messages(chat_id):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         """
#         SELECT role, content
#         FROM messages
#         WHERE chat_id = ?
#         ORDER BY id
#         """,
#         (chat_id,)
#     )

#     messages = cursor.fetchall()

#     conn.close()

#     return messages

# def get_all_chats():
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("""
#         SELECT id, title
#         FROM chats
#         ORDER BY id DESC
#     """)

#     chats = cursor.fetchall()

#     conn.close()

#     return chats

# def rename_chat(chat_id, title):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         """
#         UPDATE chats
#         SET title = ?
#         WHERE id = ?
#         """,
#         (title, chat_id),
#     )

#     conn.commit()
#     conn.close()



import sqlite3
from datetime import datetime
from pathlib import Path

# Database will always be created inside the backend/database folder
DB_NAME = Path(__file__).resolve().parent / "chat_history.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY(chat_id) REFERENCES chats(id)
    )
    """)

    conn.commit()
    conn.close()


def create_chat(title="New Chat"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats (title, created_at)
        VALUES (?, ?)
        """,
        (
            title,
            datetime.now().isoformat()
        )
    )

    chat_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return chat_id


def get_chat(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM chats
        WHERE id = ?
        """,
        (chat_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return dict(row)


def get_all_chats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM chats
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def rename_chat(chat_id, title):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET title = ?
        WHERE id = ?
        """,
        (
            title,
            chat_id
        )
    )

    conn.commit()
    conn.close()


def delete_chat(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE chat_id = ?",
        (chat_id,)
    )

    cursor.execute(
        "DELETE FROM chats WHERE id = ?",
        (chat_id,)
    )

    conn.commit()
    conn.close()


def save_message(chat_id, role, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (chat_id, role, content, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (
            chat_id,
            role,
            content,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()


def load_messages(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role,
               content,
               timestamp
        FROM messages
        WHERE chat_id = ?
        ORDER BY id
        """,
        (chat_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def save_conversation(chat_id, user_message, assistant_message):
    save_message(chat_id, "user", user_message)
    save_message(chat_id, "assistant", assistant_message)
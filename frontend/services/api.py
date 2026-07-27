
import requests
from typing import Dict, Any, List

# Your deployed backend URL
BACKEND_URL = "https://lumina-ai-fxln.onrender.com"


class BackendAPI:

    @staticmethod
    def health_check() -> bool:
        try:
            response = requests.get(
                f"{BACKEND_URL}/health",
                timeout=10
            )
            return response.status_code == 200
        except Exception:
            return False

    @staticmethod
    def send_message(
        query: str,
        thread_id: str
    ) -> Dict[str, Any]:

        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={
                "query": query,
                "thread_id": thread_id
            },
            timeout=120
        )

        response.raise_for_status()

        return response.json()

    # ------------------------
    # Chat APIs
    # ------------------------

    @staticmethod
    def get_chats() -> List[Dict]:
        response = requests.get(
            f"{BACKEND_URL}/chats"
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_chat(title="New Chat") -> Dict:
        response = requests.post(
            f"{BACKEND_URL}/chats",
            json={
                "title": title
            }
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def load_chat(chat_id: int) -> Dict:
        response = requests.get(
            f"{BACKEND_URL}/chats/{chat_id}"
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def save_message(
        chat_id: int,
        role: str,
        content: str
    ):

        response = requests.post(
            f"{BACKEND_URL}/chats/{chat_id}/messages",
            json={
                "role": role,
                "content": content
            }
        )

        response.raise_for_status()

    @staticmethod
    def rename_chat(
        chat_id: int,
        title: str
    ):

        response = requests.patch(
            f"{BACKEND_URL}/chats/{chat_id}",
            json={
                "title": title
            }
        )

        response.raise_for_status()

    @staticmethod
    def delete_chat(chat_id: int):

        response = requests.delete(
            f"{BACKEND_URL}/chats/{chat_id}"
        )

        response.raise_for_status()
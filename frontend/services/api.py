import requests
from typing import Dict, Any

# Change this if you deploy your backend
BACKEND_URL = "http://127.0.0.1:8000"


class BackendAPI:

    @staticmethod
    def health_check() -> bool:
        """
        Check if backend is running.
        """

        try:
            response = requests.get(
                f"{BACKEND_URL}/health",
                timeout=5
            )

            return response.status_code == 200

        except Exception:
            return False

    @staticmethod
    def send_message(
        query: str,
        thread_id: str
    ) -> Dict[str, Any]:
        """
        Send a chat request to the FastAPI backend.
        """

        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={
                "query": query,
                "thread_id": thread_id
            },
            timeout=120,
        )

        response.raise_for_status()

        return response.json()



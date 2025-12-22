import os
import requests

# Read API key securely
API_KEY = os.getenv("AI_API_KEY")

# Example external API endpoints (replace with your real one)
EMOTION_API_URL = "https://api.example.com/emotion"
FACE_API_URL = "https://api.example.com/face-recognition"


class APIConnector:
    def __init__(self):
        if not API_KEY:
            raise ValueError("API key not found. Set AI_API_KEY in environment variables")

        self.headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

    def call_emotion_api(self, image_path: str):
        """Send image to emotion / stress API"""
        with open(image_path, "rb") as img:
            files = {"file": img}
            response = requests.post(
                EMOTION_API_URL,
                headers=self.headers,
                files=files
            )

        if response.status_code != 200:
            raise Exception("Emotion API failed")

        return response.json()

    def call_face_api(self, image_path: str):
        """Send image to face recognition API"""
        with open(image_path, "rb") as img:
            files = {"file": img}
            response = requests.post(
                FACE_API_URL,
                headers=self.headers,
                files=files
            )

        if response.status_code != 200:
            raise Exception("Face Recognition API failed")

        return response.json()

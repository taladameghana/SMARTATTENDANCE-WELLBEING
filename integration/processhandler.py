from integration.apiconnector import APIConnector

# Optional: local AI modules
from ai_modules.face_recognition.recognizer import recognize_face
from ai_modules.emotion_stress.stress_logic import calculate_stress


class ProcessHandler:
    def __init__(self):
        self.api = APIConnector()

    def process_attendance(self, image_path: str):
        """
        1. Recognize student face
        2. Mark attendance
        """

        # Option A: Local AI
        student_name = recognize_face(image_path)

        # Option B: External API
        # response = self.api.call_face_api(image_path)
        # student_name = response.get("name")

        return {
            "student_name": student_name,
            "status": "Present"
        }

    def process_stress(self, image_path: str):
        """
        1. Detect emotion
        2. Convert emotion → stress level
        """

        # Option A: External API
        response = self.api.call_emotion_api(image_path)
        emotion = response.get("emotion")

        # Option B: Local logic
        stress_level = calculate_stress(emotion)

        return {
            "emotion": emotion,
            "stress_level": stress_level
        }


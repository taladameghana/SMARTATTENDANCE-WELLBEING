from ai_modules.face_recognition.detector import detect_faces
from ai_modules.emotion_stress.emotion_model import predict_emotion
from ai_modules.emotion_stress.stress_logic import get_stress_level

def handle_frame(image_np):
    faces = detect_faces(image_np)
    output = []

    if faces:
        for _ in faces:
            emotion = predict_emotion(None)
            stress = get_stress_level(emotion)
            output.append({"emotion": emotion, "stress": stress})

    return output


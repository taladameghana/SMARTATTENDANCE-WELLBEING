import mediapipe as mp

mp_face = mp.solutions.face_detection

def detect_faces(image_np):
    with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5) as detector:
        results = detector.process(image_np)
        return results.detections


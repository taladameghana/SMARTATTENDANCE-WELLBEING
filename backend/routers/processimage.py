from fastapi import APIRouter, File, UploadFile
import mediapipe as mp
import numpy as np
from PIL import Image
import io

router = APIRouter()

mp_face = mp.solutions.face_detection

@router.post("/image")
async def process_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_np = np.array(image)

    with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5) as detector:
        results = detector.process(image_np)

    faces_count = 0
    if results.detections:
        faces_count = len(results.detections)

    return {"faces_detected": faces_count}


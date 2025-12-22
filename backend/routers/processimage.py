from fastapi import APIRouter, File, UploadFile
import shutil
import os

router = APIRouter(prefix="/process", tags=["Image Processing"])

UPLOAD_FOLDER = "datasets/sample_uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@router.post("/upload/")
def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # Here you can call your AI modules for face recognition or stress detection
    return {"filename": file.filename, "status": "uploaded"}

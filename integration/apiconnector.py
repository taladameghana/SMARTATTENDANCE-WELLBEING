import requests

API_BASE = "http://127.0.0.1:8000"

def mark_attendance(student_id: int, present: bool = True):
    url = f"{API_BASE}/attendance/"
    payload = {"student_id": student_id, "present": present}
    response = requests.post(url, json=payload)
    return response.json()

def add_stress(student_id: int, stress_score: float):
    url = f"{API_BASE}/stress/"
    payload = {"student_id": student_id, "stress_score": stress_score}
    response = requests.post(url, json=payload)
    return response.json()

def upload_image(file_path: str):
    url = f"{API_BASE}/process/upload/"
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
    return response.json()


from integration.api_connector import mark_attendance, add_stress, upload_image
from ai_modules.face_recognition.recognizer import recognize_face
from ai_modules.emotion_stress.stress_logic import estimate_stress

def process_student_image(image_path: str):
    # Step 1: Upload image
    upload_response = upload_image(image_path)
    print("Upload Response:", upload_response)

    # Step 2: Recognize student
    student_id = recognize_face(image_path)  # your AI module should return student ID
    if not student_id:
        print("Student not recognized")
        return

    # Step 3: Mark attendance
    attendance_resp = mark_attendance(student_id)
    print("Attendance Response:", attendance_resp)

    # Step 4: Estimate stress from image
    stress_score = estimate_stress(image_path)
    stress_resp = add_stress(student_id, stress_score)
    print("Stress Response:", stress_resp)

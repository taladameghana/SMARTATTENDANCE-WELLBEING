from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import attendance, student
from pydantic import BaseModel

router = APIRouter(prefix="/attendance", tags=["Attendance"])

class AttendanceCreate(BaseModel):
    student_id: int
    present: bool = True

@router.post("/")
def mark_attendance(attendance_data: AttendanceCreate, db: Session = Depends(get_db)):
    db_student = db.query(student.Student).filter(student.Student.id == attendance_data.student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_attendance = attendance.Attendance(student_id=attendance_data.student_id, present=attendance_data.present)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return {"message": "Attendance marked", "data": {"id": new_attendance.id}}


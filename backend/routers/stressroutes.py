from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import stress, student
from pydantic import BaseModel

router = APIRouter(prefix="/stress", tags=["Stress"])

class StressCreate(BaseModel):
    student_id: int
    stress_score: float

@router.post("/")
def add_stress(stress_data: StressCreate, db: Session = Depends(get_db)):
    db_student = db.query(student.Student).filter(student.Student.id == stress_data.student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_stress = stress.Stress(student_id=stress_data.student_id, stress_score=stress_data.stress_score)
    db.add(new_stress)
    db.commit()
    db.refresh(new_stress)
    return {"message": "Stress level added", "data": {"id": new_stress.id}}


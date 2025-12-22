from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class Stress(Base):
    __tablename__ = "stress_levels"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    stress_score = Column(Float, default=0.0)

    student = relationship("Student")


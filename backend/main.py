from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import attendance_routes, stress_routes, process_image

app = FastAPI(title="Smart Attendance & Wellbeing System")

Base.metadata.create_all(bind=engine)

app.include_router(attendance_routes.router, prefix="/attendance")
app.include_router(stress_routes.router, prefix="/stress")
app.include_router(process_image.router, prefix="/process")

@app.get("/")
def root():
    return {"message": "Smart Attendance & Wellbeing API Running"}


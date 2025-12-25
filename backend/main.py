from fastapi import FastAPI
from database import Base, engine
from routers import attendance_routes, stress_routes, process_image

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Student Presence & Well-Being Monitoring API")

# Routers
app.include_router(attendance_routes.router)
app.include_router(stress_routes.router)
app.include_router(process_image.router)

@app.get("/")
def root():
    return {"message": "Smart Attendance & Wellbeing API is running"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.employee_routes import router as employee_router

app = FastAPI(title="Enterprise Employee Management System")

# ✅ CORS FIX (important)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (fix for frontend issue)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(employee_router, prefix="/api/v1")

# Health check
@app.get("/")
def root():
    return {"message": "Employee Management System API Running"}
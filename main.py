from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models


# Create database tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CodeAlpha Data Redundancy Removal System",
    description="Cloud-based system for validating data and preventing duplicate records.",
    version="1.0.0"
)


# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Handle validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "classification": "INVALID",
            "message": "The submitted data is invalid.",
            "status": "rejected",
            "errors": exc.errors()
        }
    )


# Data validation schema
class UserCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=15
    )


@app.get("/")
def home():
    return {
        "message": "Data Redundancy Removal System is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # Check whether email already exists
    existing_user = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    # Classify duplicate data
    if existing_user:
        return {
            "classification": "REDUNDANT",
            "message": "Duplicate data detected. This email already exists.",
            "status": "rejected"
        }

    # Create new unique user
    new_user = models.User(
        name=user.name,
        email=user.email,
        phone=user.phone
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "classification": "UNIQUE",
        "message": "Unique and verified data added successfully.",
        "status": "accepted",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "phone": new_user.phone
        }
    }


@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(models.User).all()

    return {
        "count": len(users),
        "users": users
    }
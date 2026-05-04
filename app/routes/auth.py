from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import SessionLocal
from models.user import User
from core.security import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])


# DB Dependency (correct way)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# REGISTER API
@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):

    # check if user already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # create new user
    user = User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "success": True,
        "message": "User created successfully",
        "user_id": user.id
    }


# LOGIN API
@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_token({"user_id": user.id})

    return {
        "success": True,
        "token": token
    }
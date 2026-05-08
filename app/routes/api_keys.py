import secrets
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.models.api_key import APIKey   # ✅ FIXED

router = APIRouter(prefix="/api-keys", tags=["API Keys"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/generate")
def generate_api_key(user_id: int, db: Session = Depends(get_db)):
    key = secrets.token_hex(16)

    api_key = APIKey(key=key, user_id=user_id)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return {"api_key": key}
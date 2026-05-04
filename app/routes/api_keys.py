from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from core.db import SessionLocal
from models.api_key import APIKey   # ✅ correct import

router = APIRouter(prefix="/keys", tags=["API Keys"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/generate")
def generate_api_key(user_id: int, db: Session = Depends(get_db)):
    new_key = str(uuid.uuid4())

    api_key = APIKey(
        key=new_key,
        user_id=user_id
    )

    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return {"api_key": new_key}
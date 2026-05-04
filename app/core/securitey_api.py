from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session

from core.db import SessionLocal
from models.api_key import APIKey
from models.usage import Usage


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_api_key(x_api_key: str = Header(...), db: Session = Depends(get_db)):
    api = db.query(APIKey).filter(APIKey.key == x_api_key).first()

    if not api:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # log usage
    usage = Usage(api_key_id=api.id, endpoint="request")
    db.add(usage)
    db.commit()

    return api
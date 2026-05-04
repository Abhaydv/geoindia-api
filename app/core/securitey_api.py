from fastapi import Header, HTTPException, Depends, Request
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.models.api_key import APIKey
from app.models.usage import Usage


# ------------------ DB ------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------ VERIFY API KEY ------------------

def verify_api_key(
    request: Request,
    x_api_key: str = Header(..., alias="x-api-key"),
    db: Session = Depends(get_db)
):
    api = db.query(APIKey).filter(APIKey.key == x_api_key).first()

    if not api:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # ------------------ LOG USAGE ------------------

    usage = Usage(
        api_key_id=api.id,
        endpoint=request.url.path   # 🔥 dynamic endpoint
    )

    db.add(usage)
    db.commit()

    return api
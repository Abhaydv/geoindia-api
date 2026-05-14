from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.db import SessionLocal

from app.models.location import (
    State,
    District,
    SubDistrict,
    Village
)

from app.models.usage import Usage

from app.core.security_api import (
    verify_api_key
)

router = APIRouter(
    prefix="/location",
    tags=["Location"]
)

# ------------------ SECURITY ------------------

security = HTTPBearer()

# ------------------ DB ------------------

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ------------------ STATES ------------------

@router.get("/states")
def get_states(
    db: Session = Depends(get_db),
    api=Depends(verify_api_key),
    credentials=Depends(security)
):

    return db.query(State).all()

# ------------------ DISTRICTS ------------------

@router.get("/districts/{state_id}")
def get_districts(
    state_id: int,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key),
    credentials=Depends(security)
):

    return db.query(District).filter(
        District.state_id == state_id
    ).all()

# ------------------ SUBDISTRICTS ------------------

@router.get("/subdistricts/{district_id}")
def get_subdistricts(
    district_id: int,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key),
    credentials=Depends(security)
):

    return db.query(SubDistrict).filter(
        SubDistrict.district_id == district_id
    ).all()

# ------------------ VILLAGES ------------------

@router.get("/villages/{district_id}")
def get_villages(
    district_id: int,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key),
    credentials=Depends(security)
):

    return db.query(Village).filter(
        Village.sub_district_id == district_id
    ).all()

# ------------------ SEARCH ------------------

@router.get("/search")
def search_location(
    q: str,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key),
    credentials=Depends(security)
):

    q = q.strip().lower()

    return db.query(Village).filter(
        func.lower(Village.name).like(
            f"%{q}%"
        )
    ).limit(10).all()

# ------------------ TEST ------------------

@router.get("/test")
def test(
    db: Session = Depends(get_db),
    api=Depends(verify_api_key),
    credentials=Depends(security)
):

    return db.query(Village).limit(10).all()

# ------------------ USAGE COUNT ------------------

@router.get("/usage-count")
def usage_count(
    db: Session = Depends(get_db),
    api=Depends(verify_api_key),
    credentials=Depends(security)
):

    total = db.query(Usage).count()

    return {
        "total_requests": total
    }

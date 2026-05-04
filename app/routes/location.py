from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.db import SessionLocal
from app.models.location import State, District, SubDistrict, Village
from app.core.security_api import verify_api_key

router = APIRouter(prefix="/location", tags=["Location"])


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
    api=Depends(verify_api_key)
):
    return db.query(State).all()


# ------------------ DISTRICTS ------------------

@router.get("/districts/{state_id}")
def get_districts(
    state_id: int,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key)
):
    return db.query(District).filter(District.state_id == state_id).all()


# ------------------ SUBDISTRICTS ------------------

@router.get("/subdistricts/{district_id}")
def get_subdistricts(
    district_id: int,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key)
):
    return db.query(SubDistrict).filter(SubDistrict.district_id == district_id).all()


# ------------------ VILLAGES ------------------

@router.get("/villages/{subdistrict_id}")
def get_villages(
    subdistrict_id: int,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key)
):
    return db.query(Village).filter(
        Village.sub_district_id == subdistrict_id
    ).all()


# ------------------ SEARCH ------------------

@router.get("/search")
def search_location(
    q: str,
    db: Session = Depends(get_db),
    api=Depends(verify_api_key)
):
    q = q.strip().lower()

    return db.query(Village).filter(
        func.lower(Village.name).like(f"%{q}%")
    ).limit(10).all()


# ------------------ TEST ------------------

@router.get("/test")
def test(
    db: Session = Depends(get_db),
    api=Depends(verify_api_key)
):
    return db.query(Village).limit(10).all()
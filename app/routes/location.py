from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from core.db import SessionLocal
from models.location import State, District, SubDistrict, Village

router = APIRouter(prefix="/location", tags=["Location"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/states")
def get_states(db: Session = Depends(get_db)):
    return db.query(State).all()


@router.get("/districts/{state_id}")
def get_districts(state_id: int, db: Session = Depends(get_db)):
    return db.query(District).filter(District.state_id == state_id).all()


@router.get("/subdistricts/{district_id}")
def get_subdistricts(district_id: int, db: Session = Depends(get_db)):
    return db.query(SubDistrict).filter(SubDistrict.district_id == district_id).all()


@router.get("/villages/{subdistrict_id}")
def get_villages(subdistrict_id: int, db: Session = Depends(get_db)):
    return db.query(Village).filter(
        Village.sub_district_id == subdistrict_id
    ).all()


@router.get("/search")
def search_location(q: str, db: Session = Depends(get_db)):
    q = q.strip().lower()

    return db.query(Village).filter(
        func.lower(Village.name).like(f"%{q}%")
    ).limit(10).all()

@router.get("/test")
def test(db: Session = Depends(get_db)):
    data = db.query(Village).limit(10).all()
    return data
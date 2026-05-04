from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base   # ✅ FIX


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)   # ✅ improvement

    districts = relationship("District", back_populates="state")


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    state_id = Column(Integer, ForeignKey("states.id"))

    state = relationship("State", back_populates="districts")
    sub_districts = relationship("SubDistrict", back_populates="district")


class SubDistrict(Base):
    __tablename__ = "sub_districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    district_id = Column(Integer, ForeignKey("districts.id"))

    district = relationship("District", back_populates="sub_districts")
    villages = relationship("Village", back_populates="sub_district")


class Village(Base):
    __tablename__ = "villages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)   # ✅ important for search
    sub_district_id = Column(Integer, ForeignKey("sub_districts.id"))

    sub_district = relationship("SubDistrict", back_populates="villages")
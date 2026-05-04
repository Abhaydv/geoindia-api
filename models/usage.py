from sqlalchemy import Column, Integer, String
from core.db import Base
class Usage(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True)
    api_key = Column(String)
    endpoint = Column(String)
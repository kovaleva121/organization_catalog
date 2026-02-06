from app.database import Base
from sqlalchemy import Column, Integer, String, Float


class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(500), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

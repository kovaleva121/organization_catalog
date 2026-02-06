from sqlalchemy import Column, String, ForeignKey, Integer
from app.database import Base
from sqlalchemy.orm import relationship


class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    parent_id = Column(Integer, ForeignKey('activities.id', ondelete='CASCADE'), nullable=True)
    level = Column(Integer, default=0, nullable=False)

    parent = relationship('Activity', remote_side=['id'], backref='children')

    organizations = relationship("Organization", secondary="organization_activity", back_populates="activities")

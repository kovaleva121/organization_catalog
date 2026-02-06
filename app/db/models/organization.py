from sqlalchemy import Column, Integer, String, ForeignKey, Table
from app.database import Base
from sqlalchemy.orm import relationship

organization_activity = Table('organization_activity', Base.metadata,
                              Column('organization_id', Integer,
                                     ForeignKey('organizations.id', ondelete='CASCADE')),
                              Column('activity_id', Integer,
                                     ForeignKey('activities.id', ondelete='CASCADE')))


class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    building_id = Column(Integer, ForeignKey('buildings.id'))
    building = relationship('Building', backref='organizations')
    activity = relationship('Activity', backref='organizations')
    phone_numbers = relationship("PhoneNumber", back_populates="organization")


class PhoneNumber(Base):
    __tablename__ = 'phone_numbers'

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey('organizations.id', ondelete='CASCADE'))
    number = Column(String(50), nullable=False)

    organization = relationship('Organization', backref='phone_number')

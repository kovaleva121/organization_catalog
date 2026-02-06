from pydantic import BaseModel
from typing import List
from app.core.models.activity import Activity
from app.core.models.building import Building


class PhoneNumberBase(BaseModel):
    number: str


class PhoneNumber(PhoneNumberBase):
    id: int

    class Config:
        from_attributes = True


class OrganizationBase(BaseModel):
    name: str
    building_id: int


class OrganizationCreate(OrganizationBase):
    phone_numbers: List[str]
    activity_ids: List[int]


class Organization(OrganizationBase):
    phone_numbers: List[PhoneNumber]
    activities: List[Activity]
    building: Building

    class Config:
        from_attributes = True

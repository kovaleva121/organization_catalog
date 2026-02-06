from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.models.building import Building
from app.dependencies import api_key_auth
from app.database import get_db
from app.crud.building import building as crud_building
from typing import List

router = APIRouter(dependencies=[Depends(api_key_auth)])


@router.get('/', response_model=List[Building])
def read_building(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    buildings = crud_building.get_multi(db, skip=skip, limit=limit)
    return buildings

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.models.activity import Activity
from app.dependencies import api_key_auth
from app.database import get_db
from app.crud.activity import activity as crud_activity
from typing import List

router = APIRouter(dependencies=[Depends(api_key_auth)])


@router.get('/', response_model=List[Activity])
def read_activities(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    buildings = crud_activity.get_multi(db, skip=skip, limit=limit)
    return buildings

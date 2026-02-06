from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.models.organization import Organization
from app.dependencies import api_key_auth
from app.database import get_db
from app.crud.organization import organization as crud_organization
from typing import List

router = APIRouter(dependencies=[Depends(api_key_auth)])


@router.get('/{organization.id}', response_model=Organization)
def read_organization(
        organization_id: int,
        db: Session = Depends(get_db)
):
    db_org = crud_organization.get_with_details(db, id=organization_id)
    if not db_org:
        raise HTTPException(status_code=404, detail='Organization not found')
    return db_org


@router.get('/', response_model=List[Organization])
def read_organizations(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    organizations = crud_organization.get_multi(db, skip=skip, limit=limit)
    return organizations

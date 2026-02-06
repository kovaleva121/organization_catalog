from app.crud.base import CRUDBase
from app.db.models.organization import Organization
from app.core.models.organization import OrganizationCreate
from sqlalchemy.orm import Session, joinedload


class CRUDOrganization(CRUDBase[Organization, OrganizationCreate, OrganizationCreate]):
    def get_with_details(self, db: Session, id: int):
        return db.query(Organization).options(joinedload(Organization.building),
                                              joinedload(Organization.activities),
                                              joinedload(Organization.phone_numbers)).filter(
            Organization.id == id).first()


organization = CRUDOrganization(Organization)

from sqlalchemy.orm import Session
from typing import List
from app.crud.base import CRUDBase
from app.db.models.activity import Activity
from app.core.models.activity import ActivityCreate


class CRUDActivity(CRUDBase[Activity, ActivityCreate, ActivityCreate]):
    def get_tree(self, db: Session) -> List[Activity]:
        return db.query(Activity).filter(Activity.level <= 3).all()


activity = CRUDActivity(Activity)

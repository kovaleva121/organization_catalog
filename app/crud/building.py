from app.crud.base import CRUDBase
from app.db.models.building import Building
from app.core.models.building import BuildingCreate


class CRUDBuilding(CRUDBase[Building, BuildingCreate, BuildingCreate]):
    pass


building = CRUDBuilding(Building)

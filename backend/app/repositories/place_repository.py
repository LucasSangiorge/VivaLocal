from sqlalchemy.orm import Session

from app.models.place import Place
from app.schemas.place import PlaceCreate

def create(db: Session, place: PlaceCreate) -> Place:
    db_place = Place(**place.model_dump())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

def get_all(db: Session, category_id: int | None = None) -> list[Place]:
    query = db.query(Place)
    if category_id is not None:
        query = query.filter(Place.category_id == category_id)
    return query.all()

def get_by_id(db: Session, place_id: int) -> Place |None:
    return db.query(Place).filter(Place.id == place_id).first()

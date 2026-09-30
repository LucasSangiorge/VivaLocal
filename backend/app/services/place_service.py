from sqlalchemy.orm import Session

from app.repositories import place_repository
from app.schemas.place import PlaceCreate


def create_place(db: Session, place: PlaceCreate):
    return place_repository.create(db, place)


def list_places(db: Session, category_id: int | None = None):
    return place_repository.get_all(db, category_id)
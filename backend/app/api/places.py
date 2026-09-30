from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.place import PlaceCreate, PlaceRead
from app.services import place_service

router = APIRouter(prefix="/places", tags=["places"])

@router.post ("/", response_model=PlaceRead)
def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    return place_service.create_place(db, place)

@router.get("/", response_model=list[PlaceRead])
def list_places(category_id: int | None = None, db: Session = Depends(get_db)):
    return place_service.list_places(db, category_id)
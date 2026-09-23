from sqlalchemy.orm import Session

from app.repositories import category_repository
from app.schemas.category import CategoryCreate


def create_category(db: Session, category: CategoryCreate):
    return category_repository.create(db, category)


def list_category(db: Session):
    return category_repository.get_all(db)

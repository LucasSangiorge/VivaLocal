from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate

def create(db: Session, category: CategoryCreate) -> Category:
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_all(db:Session) -> list[Category]:
    return db.query(Category).all()

def get_by_id(db: Session, category_id: int) -> Category | None:
    return db.query(Category).filter(Category.id == category_id).first()
    
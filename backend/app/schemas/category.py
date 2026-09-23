from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str
    slug: str

class CategoryRead(CategoryCreate):
    id: int

    model_config = {"from_attributes": True}
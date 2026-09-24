from pydantic import BaseModel

class PlaceCreate(BaseModel):
    name: str
    description: str | None = None
    address: str | None = None
    phone: str | None = None
    average_price: float | None = None
    status: str = "active"
    category_id: int


class PlaceRead(PlaceCreate):
    id: int

    model_config = {"from_attributes": True}
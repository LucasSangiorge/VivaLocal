from sqlalchemy import Column,String,Integer,Float,ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    average_price = Column(Float, nullable=True)
    status = Column(String, default="active")

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category")
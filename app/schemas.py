from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    status: Status

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    status: Status | None = None

class Product(ProductBase):
    id: int
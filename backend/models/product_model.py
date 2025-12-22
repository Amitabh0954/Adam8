from sqlalchemy import Column, Integer, String, Text, Float
from backend.models.database import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)

    def __init__(self, name: str, description: str, price: float, category: str):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __repr__(self) -> str:
        return f'<Product {self.name}>'
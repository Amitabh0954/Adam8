from typing import List
from backend.models.product_model import Product
from backend.repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def add_product(name: str, description: str, price: float, category: str) -> Product:
        if ProductRepository.get_product_by_name(name):
            raise ValueError("Product name must be unique")
        if price <= 0:
            raise ValueError("Product price must be a positive number")
        if not description:
            raise ValueError("Product description cannot be empty")

        product = Product(name=name, description=description, price=price, category=category)
        ProductRepository.add_product(product)
        return product

    @staticmethod
    def get_all_products() -> List[Product]:
        return ProductRepository.get_all_products()
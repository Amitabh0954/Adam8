from typing import Optional, List
from backend.models.product_model import Product
from backend import db

class ProductRepository:

    @staticmethod
    def get_product_by_id(product_id: int) -> Optional[Product]:
        return Product.query.get(product_id)

    @staticmethod
    def get_product_by_name(name: str) -> Optional[Product]:
        return Product.query.filter_by(name=name).first()

    @staticmethod
    def add_product(product: Product) -> None:
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update_product() -> None:
        db.session.commit()

    @staticmethod
    def delete_product(product: Product) -> None:
        db.session.delete(product)
        db.session.commit()

    @staticmethod
    def get_all_products() -> List[Product]:
        return Product.query.all()
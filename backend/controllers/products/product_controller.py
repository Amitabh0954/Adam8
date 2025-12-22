from flask import Blueprint, request, jsonify
from backend.services.products.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category = data.get('category')
    if not name or not description or price is None or not category:
        return jsonify({'message': 'All fields are required'}), 400
    try:
        product = ProductService.add_product(name, description, price, category)
        return jsonify({'message': 'Product added successfully', 'product': {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'category': product.category}}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@product_bp.route('/products', methods=['GET'])
def get_all_products():
    products = ProductService.get_all_products()
    result = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'category': product.category} for product in products]
    return jsonify(result), 200
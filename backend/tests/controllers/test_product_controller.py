import json
from flask import url_for
from backend import create_app, db
from backend.models.product_model import Product

app = create_app("testing")

def test_add_product(client):
    url = url_for('product_bp.add_product')
    data = {
        'name': 'testproduct',
        'description': 'Test product description',
        'price': 9.99,
        'category': 'testcategory'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 201
    assert response.json['product']['name'] == 'testproduct'
    assert response.json['product']['price'] == 9.99

def test_add_product_with_existing_name(client):
    product = Product(name='testproduct', description='Test product description', price=9.99, category='testcategory')
    db.session.add(product)
    db.session.commit()
    url = url_for('product_bp.add_product')
    data = {
        'name': 'testproduct',
        'description': 'Another product description',
        'price': 19.99,
        'category': 'anothercategory'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json['message'] == 'Product name must be unique'

def test_add_product_with_invalid_price(client):
    url = url_for('product_bp.add_product')
    data = {
        'name': 'testproduct',
        'description': 'Test product description',
        'price': -10,
        'category': 'testcategory'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json['message'] == 'Product price must be a positive number'

def test_get_all_products(client):
    product1 = Product(name='testproduct1', description='Description1', price=9.99, category='category1')
    product2 = Product(name='testproduct2', description='Description2', price=19.99, category='category2')
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()
    url = url_for('product_bp.get_all_products')
    response = client.get(url)
    
    assert response.status_code == 200
    products = response.json
    assert len(products) == 2
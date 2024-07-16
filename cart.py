from flask import Blueprint, request, jsonify
from app import db
from app.models import CartItem

bp = Blueprint('cart', __name__, url_prefix='/cart')

@bp.route('/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    new_item = CartItem(
        product_id=data['product_id'],
        name=data['name'],
        price=data['price'],
        image_url=data['image_url']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added to cart"}), 201

@bp.route('/items', methods=['GET'])
def get_cart_items():
    cart_items = CartItem.query.all()
    return jsonify([{
        "product_id": item.product_id,
        "name": item.name,
        "price": item.price,
        "image_url": item.image_url
    } for item in cart_items]), 200

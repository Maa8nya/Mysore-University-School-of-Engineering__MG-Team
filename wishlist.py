from flask import Blueprint, request, jsonify
from app import db
from app.models import WishlistItem

bp = Blueprint('wishlist', __name__, url_prefix='/wishlist')

@bp.route('/add', methods=['POST'])
def add_to_wishlist():
    data = request.get_json()
    new_item = WishlistItem(
        product_id=data['product_id'],
        name=data['name'],
        price=data['price'],
        image_url=data['image_url']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added to wishlist"}), 201

@bp.route('/items', methods=['GET'])
def get_wishlist_items():
    wishlist_items = WishlistItem.query.all()
    return jsonify([{
        "product_id": item.product_id,
        "name": item.name,
        "price": item.price,
        "image_url": item.image_url
    } for item in wishlist_items]), 200

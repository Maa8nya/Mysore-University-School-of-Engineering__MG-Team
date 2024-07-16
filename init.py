from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # Import Blueprints
        from .routes import cart, wishlist

        # Register Blueprints
        app.register_blueprint(cart.bp)
        app.register_blueprint(wishlist.bp)

        # Create Database Tables
        db.create_all()

    return app

import schedule
import time
from threading import Thread
from app.models import CartItem, WishlistItem
from app.notifications.notifier import send_notification
from app import db

# Mock price fetching function
def fetch_latest_prices():
    return {
        '123': 89.99,
        '456': 139.99
    }

def check_price_drops():
    latest_prices = fetch_latest_prices()
    cart_items = CartItem.query.all()
    wishlist_items = WishlistItem.query.all()

    for item in cart_items + wishlist_items:
        if item.product_id in latest_prices and latest_prices[item.product_id] < item.price:
            send_notification(item.name, item.price, latest_prices[item.product_id])

def send_notification(name, old_price, new_price):
    print(f'Price Drop Alert: {name} dropped from ${old_price} to ${new_price}')

def run_scheduler():
    schedule.every(10).minutes.do(check_price_drops)
    while True:
        schedule.run_pending()
        time.sleep(1)

scheduler_thread = Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

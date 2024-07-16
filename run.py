from app.init import create_app
from threading import Thread
from app.services.price_checker import run_scheduler

app = create_app()

if __name__ == '__main__':
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    app.run(debug=True)

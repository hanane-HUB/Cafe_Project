from models.orders import Order
from core.db_manager import session


def fetch_orders():
    return session.query(Order).all()

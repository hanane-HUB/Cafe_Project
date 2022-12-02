from models.receipts import Receipt
from core.db_manager import session


def fetch_recipts():
    return session.query(Receipt).all()

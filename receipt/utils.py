import sqlalchemy
from core.db_manager import session
from models.receipts import Receipt
from models.orders import Order


def get_id():
    id = session.query(Receipt).order_by(sqlalchemy.desc(Receipt.id)).first()
    return id + 1


def get_receipt(id):
    res = session.query(Receipt).filter_by(user_id=id).all()
    return list(res)


def total_amount(rec_id):
    orders = session.query(Order).filter_by(receipt_id=rec_id).all()
    total = 0
    for order in orders:
        total += order.price
    return total


def add_receipt(id, table_id, user_id, total_price, pay):
    receipt = Receipt(id, table_id, user_id, total_price, pay)
    session.add(receipt)
    session.commit()

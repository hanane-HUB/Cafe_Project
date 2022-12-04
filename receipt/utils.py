import sqlalchemy
from core.db_manager import session
from models.receipts import Receipt
from models.orders import Order


def get_receipt(id):
    res = session.query(Receipt).filter_by(user_id=id).all()
    return list(res)


def check_user_receipt(id):
    user_receipts = session.query(Receipt).filter_by(user_id=id).all()
    for receipt in user_receipts:
        if bool(receipt.pay) == False:
            return receipt.id


def total_amount(rec_id):
    orders = session.query(Order).filter_by(receipt_id=rec_id).all()
    total = 0
    for order in orders:
        total += order.price
    return total


def add_receipt(table_id, user_id, total_price, pay):
    receipt = Receipt(table_id=table_id, user_id=user_id, total_price=total_price, pay=pay)
    session.add(receipt)
    session.commit()

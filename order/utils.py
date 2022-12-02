from flask import request
from models.orders import Order
from core.db_manager import session


def get_order_list():
    return session.query(Order).all()


def change_status(order_id):
    order = session.query(Order).filter(Order.id == order_id)
    status = request.form["status_order"]
    for j in order:
        j.status = status
    session.commit()

def add_order(item_id, receid_id, number, status, time_stamp):
    order = Order(item_id=item_id,receid_id=receid_id, number=number, status=status, time_stamp=time_stamp)
    session.add(order)
    session.commit()
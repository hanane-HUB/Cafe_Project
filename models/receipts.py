from core.db_manager import Base, session
from sqlalchemy import Column, Integer, Float
from sqlalchemy import create_engine, ForeignKey
from models.orders import Order
from models.table import Table
from models.user import User


class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column('receipt_id', Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(Order.id))
    table_id = Column(Integer, ForeignKey(Table.id))
    user_id = Column(Integer, ForeignKey(User.id))
    total_price = Column(Float)



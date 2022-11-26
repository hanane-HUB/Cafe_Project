from core.db_manager import Base
from sqlalchemy import Column, Integer, String, Date, ARRAY, Float
from sqlalchemy import create_engine, ForeignKey
from menu_items import MenuItems


class Order(Base):
    __tablename__ = 'orders'
    # todo: cahnge menu_id to order_id
    id = Column('menu_id', Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey(MenuItems.id))
    number = Column(Integer)
    status = Column(String(50))
    time_stamp = Column(String(50))



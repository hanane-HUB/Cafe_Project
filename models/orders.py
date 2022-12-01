from core.db_manager import Base, engine, session
from sqlalchemy import Column, Integer, String, Date, ARRAY, Float
from sqlalchemy import create_engine, ForeignKey
from models.menu_items import MenuItems
from models.receipts import Receipt


class Order(Base):
    __tablename__ = 'orders'
    id = Column('order_id', Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey(MenuItems.id))
    receid_id = Column(Integer, ForeignKey(Receipt.id))
    number = Column(Integer)
    status = Column(String(50))
    time_stamp = Column(String(50))

    def __init__(self, item_id, receid_id, number, status, time_stamp):
        self.item_id = item_id
        self.receid_id = receid_id
        self.number = number
        self.status = status
        self.time_stamp = time_stamp


# Base.metadata.create_all(engine)
# session.commit()



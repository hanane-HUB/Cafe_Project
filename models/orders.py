from Cafe_Project.core.db_manager import Base, engine, session
from sqlalchemy import Column, Integer, String, Date, ARRAY, Float
from sqlalchemy import create_engine, ForeignKey
from Cafe_Project.models.menu_items import MenuItems
from Cafe_Project.models.receipts import Receipt


class Order(Base):
    __tablename__ = 'orders'
    id = Column('order_id', Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey(MenuItems.id))
    receid_id = Column(Integer, ForeignKey(Receipt.id))
    number = Column(Integer)
    status = Column(String(50))
    time_stamp = Column(String(50))


# Base.metadata.create_all(engine)
# session.commit()



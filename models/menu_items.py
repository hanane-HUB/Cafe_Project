from core.db_manager import Base
from sqlalchemy import Column, Integer, String, Date, Float


class MenuItems(Base):
    __tablename__ = 'menu_items'
    id = Column('menu_id', Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Float)
    category = Column(String(30))



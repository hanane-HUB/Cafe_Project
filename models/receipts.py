from core.db_manager import Base, session,engine
from sqlalchemy import Column, Integer, Float, Boolean
from sqlalchemy import create_engine, ForeignKey
from models.table import Table
from models.user import User


class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column('receipt_id', Integer, primary_key=True)
    table_id = Column(Integer, ForeignKey(Table.id))
    user_id = Column(Integer, ForeignKey(User.id))
    total_price = Column(Float)
    pay = Column(Boolean)



# Base.metadata.create_all(engine)
# session.commit()

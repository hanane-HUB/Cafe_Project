from core.db_manager import Base, session
from sqlalchemy import Column, Integer, String, ARRAY


class Table(Base):
    __tablename__ = 'tables'
    id = Column('table_id', Integer(), primary_key=True)
    position = Column(ARRAY(Integer))


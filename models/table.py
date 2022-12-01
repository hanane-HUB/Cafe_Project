from core.db_manager import Base, session, engine
from sqlalchemy import Column, Integer, String, ARRAY, Boolean


class Table(Base):
    __tablename__ = 'tables'
    id = Column('table_id', Integer(), primary_key=True)
    position = Column(ARRAY(Integer))
    available = Column(Boolean)


# Base.metadata.create_all(engine)
# session.commit()


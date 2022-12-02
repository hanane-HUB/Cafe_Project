from core.db_manager import Base, session, engine
from sqlalchemy import Column, Integer, String, ARRAY


class Table(Base):
    __tablename__ = 'tables'
    id = Column('table_id', Integer, autoincrement=True , primary_key=True)
    position = Column(String(50))
    status = Column(String(50))

# table_list = session.query(Table).all()
# print(table_list)


# Base.metadata.create_all(engine)
# session.commit()

# table=Table(position='gharb' ,status='Reserved' )
# session.add(table)
# session.commit()


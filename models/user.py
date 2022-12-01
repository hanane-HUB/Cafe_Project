from sqlalchemy import Column, Integer, String
from core.db_manager import Base, session, engine


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    username = Column('user_name', String(30))
    first_name = Column(String(15))
    last_name = Column(String(15))
    phone = Column(String(11))
    email = Column(String(100))
    password = Column(String(50))

    def __init__(self, username, fname, lname, phone, email, password):
        self.username = username
        self.first_name = fname
        self.last_name = lname
        self.phone = phone
        self.email = email
        self.password = password


# Base.metadata.create_all(engine)
# session.commit()
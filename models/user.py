from core.db_manager import Base, session
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer(), primary_key=True)
    # todo: id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    first_name = Column(String(15))
    last_name = Column(String(15))
    phone = Column(String(11))
    email = Column(String(100))
    password = Column(String(50))

    def __init__(self, id, fname, lname, phone, email, password):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.phone = phone
        self.email = email
        self.password = password

    @staticmethod
    def add(id, fname, lname, phone, email, password):
        user = User(id, fname, lname, phone, email, password)
        session.add(user)

        session.commit()



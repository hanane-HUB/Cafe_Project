from sqlalchemy import Column, Integer, String
from Cafe_Project.core.db_manager import Base, session, engine


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer(), primary_key=True)
    # id = Column('user_id', Integer(), primary_key=True, autoincrement=True)
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

    @staticmethod
    def check_login(id, password):
        # question = session.query(User).filter_by(id=1).all()
        question = session.query(User).all()
        for q in question:
            if str(q.id) == id:
                if str(q.password) == password:
                    return True

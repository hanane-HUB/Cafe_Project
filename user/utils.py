from models.user import User
from core.db_manager import session


def add_user(username, fname, lname, phone, email, password):
    user = User(username=username, fname=fname, lname=lname, phone=phone, email=email, password=password)
    session.add(user)
    session.commit()


def check_login(username, password):
    # question = session.query(User).filter_by(id=1).all()
    users = session.query(User).all()
    for q in users:
        if str(q.username) == username:
            if str(q.password) == password:
                return True


def check_username(username):
    users = session.query(User).all()
    for q in users:
        if str(q.username) == username:
            return False
    return True

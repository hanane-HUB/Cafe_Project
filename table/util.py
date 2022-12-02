from models.table import Table
from core.db_manager import session


def add_table(position, status):
    table = Table(position=position, status=status)
    session.add(table)
    session.commit()


def check_table_status(table_id):
    tables=session.query(Table).all()
    for q in tables:
        if str(q.table_id) == table_id:
            if str(q.status) == 'Reserved' or str(q.status) == 'Full':
                return False
        return True

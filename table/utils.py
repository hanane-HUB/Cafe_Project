from core.db_manager import session
from models.table import Table


def assign_table():
    table = session.query(Table).filter_by(available=True).first()
    if table:
        return table.id
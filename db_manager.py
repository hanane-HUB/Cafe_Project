from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine, ForeignKey

engine = create_engine('postgresql://postgres:hana7988@127.0.0.1:5433/cafe')
connection = engine.connect()
Base = declarative_base()
Session = session.sessionmaker(bind=engine)
session = Session()

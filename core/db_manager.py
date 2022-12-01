from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine, ForeignKey

engine = create_engine('postgresql://postgres:hana7988@127.0.0.1:5433/cafe')
connection = engine.connect()
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = db_session.query_property()
Session = session.sessionmaker(bind=engine)
session = Session()

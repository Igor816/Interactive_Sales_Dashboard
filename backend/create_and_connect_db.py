from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.model import Base

data_url = 'postgresql+psycopg://postgres:89936684600Ant@127.0.0.1:5432/sales_db'
engine = create_engine(data_url)

session = sessionmaker(bind=engine, class_=Session)

def create_db_and_tables() -> None:
	Base.metadata.create_all(engine)


create_db_and_tables()

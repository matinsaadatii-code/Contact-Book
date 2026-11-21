import psycopg
from psycopg.rows import dict_row
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_username}:{settings.db_password}@{settings.db_ip}:{settings.db_port}/{settings.db_name}'

enigine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=enigine)
Base = declarative_base()
connection = None


def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()


connection = psycopg.connect(
    host=f'{settings.db_ip}', 
    port=f'{settings.db_port}', 
    dbname=f'{settings.db_name}', 
    user=f'{settings.db_username}', 
    password=f'{settings.db_password}', 
    row_factory=dict_row
)

print(enigine)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from . import models


engine = create_engine("sqlite:///./database/test.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
Base = declarative_base()

def _create_database():
    Base.metadata.create_all(engine)

async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

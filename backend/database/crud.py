from datetime import datetime, date
from sqlalchemy.orm import sessionmaker
from . import models, schemas


async def create_post(db: sessionmaker, payload: schemas.PostIn):
    data = payload.dict()
    db_post = models.Post(**data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post_by_id(db: sessionmaker, id: int):
    return db.query(models.Post).filter(models.Post.id==id).first()

def get_all_post(db: sessionmaker):
    return db.query(models.Post).all()

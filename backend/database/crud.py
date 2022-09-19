from datetime import datetime, date
from sqlalchemy.orm import sessionmaker
from . import models, schemas
import json

def _convert(how, obj):
    match how:
        case 'list to str':
            new_obj = str(obj).replace("'", '"')
        case 'str to list':
            new_obj = list(json.loads(obj))
    return new_obj


async def create_post(db: sessionmaker, payload: schemas.PostCreate):
    # convert list to string for the INPUT DB
    data = payload.dict()
    data['subject'] = _convert('list to str', data['subject'])
    data['topics'] = _convert('list to str', data['topics'])
    # INPUT DB
    db_post = models.Post(**data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    # convert string to list for the OUTPUT RESPONSE
    db_post = db_post.__dict__
    db_post['subject'] = _convert('str to list', db_post['subject'])
    db_post['topics'] = _convert('str to list', db_post['topics'])

    return db_post

async def update_post(db: sessionmaker, payload: schemas.PostUpdate):
    data = payload.dict()
    data['subject'] = _convert('list to str', data['subject'])
    data['topics'] = _convert('list to str', data['topics'])

    query_obj = db.query(models.Post).filter(models.Post.id==payload.id)
    db_post = query_obj.first()
    query_obj.update(data)
    db.commit()

    db_post = db_post.__dict__
    db_post['subject'] = _convert('str to list', db_post['subject'])
    db_post['topics'] = _convert('str to list', db_post['topics'])
    return db_post

async def get_post_by_id(db: sessionmaker, id: int):
    db_post = db.query(models.Post).filter(models.Post.id==id).first()

    if db_post == None:
        return None
    db_post = db_post.__dict__
    db_post['subject'] = _convert('str to list', db_post['subject'])
    db_post['topics'] = _convert('str to list', db_post['topics'])
    return db_post

async def get_all_post(db: sessionmaker):
    db_posts = db.query(models.Post).all()
    for db_post in db_posts:
        db_post = db_post.__dict__
        db_post['subject'] = _convert('str to list', db_post['subject'])
        db_post['topics'] = _convert('str to list', db_post['topics'])
    return db_posts

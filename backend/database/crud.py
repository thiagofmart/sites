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
    db_post = models.Post(
        title=data['title'],
        subject=_convert('list to str', data['subject']),
        description=data['description'],
        image=data['image'],
        author=data['author'],
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    for topico in data['topics']:
        db_topic = models.Topic(
            post_id=db_post.id,
            title=topico['title'],
            content=topico['content'],
        )
        db.add(db_topic)
    db.commit()
    db.refresh(db_post)
    db_post = db_post.__dict__
    db_post['subject'] = _convert('str to list', db_post['subject'])
    return db_post

async def update_post(db: sessionmaker, payload: schemas.PostUpdate):
    data = payload.dict()
    data['subject'] = _convert('list to str', data['subject'])

    query_obj = db.query(models.Post).filter(models.Post.id==payload.id)
    db_post = query_obj.first()
    query_obj.update(data)
    db.commit()
    db.refresh(db_post)

    db_post = db_post.__dict__
    db_post['subject'] = _convert('str to list', db_post['subject'])
    return db_post

async def get_post_by_id(db: sessionmaker, id: int):
    db_post = db.query(models.Post).filter(models.Post.id==id).first()
    if db_post == None:
        return None
    db_post = db_post.__dict__
    db_post['subject'] = _convert('str to list', db_post['subject'])
    return db_post

async def get_topic_by_id(db: sessionmaker, id: int):
    db_topic = db.query(models.Topic).filter(models.Topic.id==id).first()
    if db_topic == None:
        return None
    return db_topic

async def get_all_topics_by_post_id(db: sessionmaker, id: int):
    db_topics = db.query(models.Topic).filter(models.Topic.post_id==id).all()
    if db_topics == None:
        return None
    return db_topics

async def get_all_posts(db: sessionmaker):
    db_posts = db.query(models.Post).all()
    for db_post in db_posts:
        db_post = db_post.__dict__
        db_post['subject'] = _convert('str to list', db_post['subject'])
    return db_posts

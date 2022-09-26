from database import schemas, crud, database
from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
import aspose.words as aw
import os


#uvicorn app:app --reload
PATH_ROOT = os.path.dirname(os.path.abspath(__name__))
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://127.0.0.1:3000',
        'http://127.0.0.1:55121',
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
database._create_database()


@app.post('/post/create/', response_model=schemas.Post)
async def create_post(payload: schemas.PostCreate, db: sessionmaker=Depends(database.get_db)):
    db_post = await crud.create_post(db=db, payload=payload)
    return db_post
@app.post('/post/update/', response_model=schemas.Post)
async def update_post(payload: schemas.PostUpdate, db: sessionmaker=Depends(database.get_db)):
    db_post = await crud.update_post(db=db, payload=payload)
    return db_post


@app.get('/all/posts/', response_model=list[schemas.Post])
async def get_all_posts(db: sessionmaker=Depends(database.get_db)):
    response = await crud.get_all_posts(db=db)
    return response

@app.get('/topic/by_id/', response_model=schemas.Topic)
async def get_topic_by_id(id: int|str, db: sessionmaker=Depends(database.get_db)):
    response = await crud.get_topic_by_id(db=db, id=id)
    return response

@app.get('/all/topics/by_post_id/', response_model=list[schemas.Topic])
async def get_all_topics_by_post_id(id: int|str, db: sessionmaker=Depends(database.get_db)):
    response = await crud.get_all_topics_by_post_id(db=db, id=id)
    return response

@app.get('/post/by_id/', response_model=schemas.Post|None)
async def get_post_by_id(id: int|str, db: sessionmaker=Depends(database.get_db)):
    response = await crud.get_post_by_id(db=db, id=id)
    return response

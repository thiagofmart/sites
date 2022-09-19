from database import schemas, crud, database
from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
import os


#uvicorn app:app --reload
PATH_ROOT = os.path.dirname(os.path.abspath(__name__))
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:3000',],
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


@app.get('/post/get_all/', response_model=list[schemas.Post])
async def get_posts(db: sessionmaker=Depends(database.get_db)):
    response = await crud.get_all_post(db=db)
    return response

@app.get('/post/by_id/', response_model=schemas.Post|None)
async def get_post_by_id(id: int|str, db: sessionmaker=Depends(database.get_db)):
    response = await crud.get_post_by_id(db=db, id=id)
    return response

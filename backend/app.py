from database import schemas, crud, database
from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
import os


#uvicorn app:app --reload
PATH_ROOT = os.path.dirname(os.path.abspath(__name__))
app = FastAPI()
database._create_database()


@app.post('/posts/create/', response_model=list)
async def create_posts(payload: schemas.PostIn, db: sessionmaker=Depends(database.get_db)):
    response = [
        {
            "subject": ["math", "IoT"],
            "title": "Article 1",
            "description": "This article will show you something really cool",
            "topics": [
                {
                    "title": "title"
                },
            ],
        },
    ]
    return response
@app.get('/posts/get/', response_model=list)
async def get_posts(db: sessionmaker=Depends(database.get_db)):
    response = [
        {
            "subject": ["math", "IoT"],
            "title": "Article 1",
            "description": "This article will show you something really cool",
            "topics": [
                {
                    "title": "title"
                },
            ],
        },
    ]
    return response

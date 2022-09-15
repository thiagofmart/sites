from pydantic import BaseModel
from datetime import datetime


class Topic(BaseModel):
    title: str
    content: str

class PostCreate(Topic):
    subject: list[str] #must be a list stringfied like '["topico1", "topico2", "topico3"]'
    description: str
    topics: list[Topic] #must be a list stringfied like '["topico1", "topico2", "topico3"]'
    author: str

class PostUpdate(PostCreate):
    id: int

class Post(PostCreate):
    id: int
    posted_at: datetime
    updated_at: datetime | None
    class Config:
        orm_mode=True

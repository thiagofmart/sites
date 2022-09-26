from pydantic import BaseModel
from datetime import datetime



class TopicCreate(BaseModel):
    title: str
    content: bytes

class TopicAppend(TopicCreate):
    post_id: int

class Topic(TopicCreate):
    id: int
    class Config:
        orm_mode=True


class PostCreate(BaseModel):
    title: str
    subject: list[str] #must be a list stringfied like '["topico1", "topico2", "topico3"]'
    description: str
    topics: list[TopicCreate] #must be a list stringfied like '["topico1", "topico2", "topico3"]'
    image: bytes
    author: str


class PostUpdate(BaseModel):
    id: int
    title: str
    subject: list[str] #must be a list stringfied like '["topico1", "topico2", "topico3"]'
    description: str
    image: bytes
    author: str


class Post(BaseModel):
    id: int
    subject: list[str] #must be a list stringfied like '["topico1", "topico2", "topico3"]'
    title: str
    description: str
    image: bytes
    author: str
    posted_at: datetime
    updated_at: datetime | None
    class Config:
        orm_mode=True

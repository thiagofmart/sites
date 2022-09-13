from pydantic import BaseModel
from typing import List
from datetime import datetime


class Topic(BaseModel):
    title: str
    content: str

class PostIn(Topic):
    subject: List[str]
    description: str
    topics: str #must be a list stringfy like '["topico1", "topico2", "topico3"]'

class Post(Topic):
    id: int
    subject: List[str]
    description: str
    topics: List[Topic] #must be a list stringfy like '["topico1", "topico2", "topico3"]'
    author: str
    posted_at: datetime
    updated_at: datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import engine
from .database import Base


class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    title = Column(String)
    description = Column(String)
    content = Column(String)
    topics = Column(String)
    author = Column(String)
    posted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

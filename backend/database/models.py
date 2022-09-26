from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, LargeBinary
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
    image = Column(LargeBinary)
    author = Column(String)
    posted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    topics = relationship(
            "Topic", 
            backref='post',
            order_by='Topic.id',
            cascade="all, delete-orphan",
            )


class Topic(Base):
    __tablename__='topic'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    title = Column(String)
    content = Column(String)
    posted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

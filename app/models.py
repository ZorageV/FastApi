from sqlalchemy import Boolean, Column, Integer, String, true
from .database import Base,sessionLocal,engine


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,default=True)
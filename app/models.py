from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.sql.expression import text
from .database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=True)
    content = Column(String,nullable=True)
    published = Column(Boolean,default=True)
    created_at = Column(TIMESTAMP(timezone=False),nullable=False,server_default=text("NOW()"))
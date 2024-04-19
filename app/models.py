from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.sql.expression import text
from .database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,default=False)
    created_at = Column(TIMESTAMP(timezone=False),nullable=False,server_default=text("NOW()"))
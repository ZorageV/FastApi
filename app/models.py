from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,default=False)
    created_at = Column(TIMESTAMP(timezone=False),nullable=False,server_default=text("NOW()"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("User", back_populates="posts")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=False),nullable=False,server_default=text("NOW()"))

    posts = relationship("Post", back_populates="user")
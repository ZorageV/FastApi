from random import randint
import time
from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from .database import engine,SessionLocal
from . import models

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True


my_posts = [
    {
        "id": 1,
        "title": "Post1",
        "content": "Content of post1",
        "published": True,
        "rating": 5,
    },
    {
        "id": 2,
        "title": "Post2",
        "content": "Content of post2",
        "published": False,
        "rating": 3,
    },
]

def index_post(id):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            return i
    return -1

@app.get("/")
def root():
    return {"Hello": "I am Manjeet Singh"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"Data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post = cursor.fetchone() 
    conn.commit()
    return {"Data": new_post}


@app.get("/posts/{id}")
def get_posts(id: int):
    try:
        cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id),))
        post = cursor.fetchone()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return {"Post details" : post}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *;""",(str(id),))
    post = cursor.fetchone()
    conn.commit()
    print(f"\n\n {post} \n\n")
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}",status_code=status.HTTP_201_CREATED)
def update_post(id:int, post:Post):
    post = post.model_dump()
    cursor.execute("""UPDATE posts 
                    SET title = %s,content = %s,published = %s
                    WHERE id = %s RETURNING *;""",(post['title'],post['content'],post['published'],str(id),))
    up_post = cursor.fetchone()
    conn.commit()
    print(f"\n\n {up_post} \n\n")
    if not update_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return up_post
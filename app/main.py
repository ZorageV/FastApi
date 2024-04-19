from typing import List
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
import psycopg2
from psycopg2.extras import RealDictCursor
from .database import engine,get_db
from . import models,schemas
from sqlalchemy.orm import Session
from app import database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="zorage",cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("DB connected")
        break
    except Exception as error:
        print("Connecting to DB failed")


@app.get("/")
def root():
    return {"Hello": "I am Manjeet Singh"}

@app.get("/posts",response_model=List[schemas.Post])
def get_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,db : Session = Depends(get_db)):
    new_post = models.Post(**(post.model_dump()))
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/posts/{id}",status_code=status.HTTP_200_OK,response_model = schemas.Post)
def get_posts(id: int,db : Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return post


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db : Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    post.delete(synchronize_session=False)
    db.commit()
    print(f"\n\n {post} \n\n")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def update_post(id:int, updated_post:schemas.PostCreate,db : Session = Depends(get_db)):
    up_query = db.query(models.Post).filter(models.Post.id == id)
    post = up_query.first()
    if not update_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    up_query.update(updated_post.model_dump(),synchronize_session= False)
    db.commit()
    db.refresh(post)
    print(f"\n\n {post} \n\n")
    return post


@app.get("/sqlalchemy")
def test_post(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"Data" : posts}
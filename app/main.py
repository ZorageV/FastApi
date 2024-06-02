import uvicorn
from typing import List
from fastapi import Depends, FastAPI, HTTPException, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
from  .database import engine,get_db
from . import models,schemas
from .routers import posts,users,auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

while True:
    try:
        conn = psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="zorage",cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("DB connected")
        break
    except Exception as error:
        print("Connecting to DB failed")

from ast import Delete
from random import randint
from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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
    return {"Data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_post: Post):
    new_post_dict = new_post.model_dump()
    new_post_dict["id"] = randint(0, 1000)
    my_posts.append(new_post_dict)

    return {"Data": new_post_dict}


@app.get("/posts/{id}")
def get_posts(id: int):
    index = index_post(id)
    if index == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return {"Post details": my_posts[index]}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = index_post(id)
    if index == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    else:
        my_posts.pop(index)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}",status_code=status.HTTP_201_CREATED)
def update_post(id:int, post:Post):
    index = index_post(id)
    if index == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    else:
        post = post.model_dump()
        post["id"] = id
        my_posts[index] = post
        return {"updated" : post}
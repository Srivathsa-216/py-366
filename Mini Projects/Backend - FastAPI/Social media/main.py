from fastapi import FastAPI
from fastapi.params import Body

from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"id": 1, "title": "Chocolate of India", "content": "Dairy Milk chocolate will always be the top priority of customers in India."},
    {"id": 2, "title": "Leader to Remember", "content": "Modi is or will always be rememberd as the number 1 global leader."}
]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts }

@app.post("/posts")
def create_post(post: Post):
    print(post)
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 999999999)
    my_posts.append(post_dict)
    return {"new_post" : 
            {"status":"Post Created Successfully",
            "details": f"title : {post.title} , content : {post.content}",
            "published": f"{post.published}",
            "rating": f"{post.rating}"}
            }

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}

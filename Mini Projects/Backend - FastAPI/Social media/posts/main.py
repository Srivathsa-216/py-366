from fastapi import FastAPI, status, HTTPException, Response

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
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts }

@app.post("/posts", status_code=status.HTTP_201_CREATED)
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

    if not (post := find_post(id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id : {id} was not found")

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} doesnt exist")

    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} doesnt exist")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"Data Updated Succesfully" : post_dict}
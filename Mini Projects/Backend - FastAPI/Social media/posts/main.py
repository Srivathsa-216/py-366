from fastapi import FastAPI, status, HTTPException, Response

from pydantic import BaseModel
from typing import Optional
from random import randrange
import mysql.connector


app = FastAPI()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="posts_fastapi"
)

# Create a cursor object
mycursor = mydb.cursor()

# Define the SQL query to retrieve all records
#sql = "SELECT * FROM posts"

# Execute the query
#mycursor.execute(sql)

# Fetch all results
#myresult = mycursor.fetchall()

# Print the results (modify this section for your specific needs)
# print("Post Details:")
# for row in myresult:
#   print(row)

# Close the cursor and connection (important)
# mycursor.close()
# mydb.close()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# my_posts = [
#     {"id": 1, "title": "Chocolate of India", "content": "Dairy Milk chocolate will always be the top priority of customers in India."},
#     {"id": 2, "title": "Leader to Remember", "content": "Modi is or will always be rememberd as the number 1 global leader."}
# ]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    statement = "SELECT * FROM posts"
    mycursor.execute(statement)
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    
    my_posts = [
        {col: val for val, col in zip(row, column_names)}
        for row in myresult
    ]

    return {"details" : my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    #print(post)
    query = "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)"
    mycursor.execute(query, (post.title, post.content, post.published))
    mydb.commit()
    return { "Record inserted to DB successfuly"}

@app.get("/posts/{id}")
def get_post(id: int):
    query = f"select * from posts where id = {id}"
    mycursor.execute(query)
    if not (post := mycursor.fetchall()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id : {id} was not found")

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    query = f"delete from posts where id = {id}"
    mycursor.execute(query)
    if mycursor.rowcount <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} doesnt exist")

    mydb.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    query = "update posts set title = %s, content = %s, published = %s where id = %s"
    mycursor.execute(query, (post.title, post.content, post.published, str(id)))
    mydb.commit()

    if mycursor.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} doesnt exist")

    return {"Data Updated Succesfully" : f"{mycursor.rowcount} records affected"}
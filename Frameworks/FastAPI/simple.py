from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome to the FastAPI world!!!, {name}"

food_items = {
    'Indian': ['Dosa', 'Ragiball'],
    'American': ['Hotdog', 'Apple Pie'],
    'Italian': ['Ravioli', 'Pizza']
}

class AvailableCuisines(str, Enum):
    Indian = "Indian"
    American = "American"
    Italian = "Italian"

@app.get("/fooditems/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)
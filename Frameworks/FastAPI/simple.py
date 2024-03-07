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

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("get_coupon/{code}")
async def get_items(code: int):
    return { 'discount_amount': coupon_code.get(code)}
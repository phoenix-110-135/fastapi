from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
import random, json

app = FastAPI(
    title="FAL API",
    description="A simple API to get random Hafez poems",
    version="1.0.0",
)

with open("fals.json", "r", encoding="utf-8") as f:
    Hafez_Fals = json.load(f)

def find_fal_by_id(fal_id):
    for fal in Hafez_Fals:
        if fal.get("id") == fal_id:
            return fal
    return None

@app.get("/")
async def read_root():
    return {"message": "welcome to FAL hafez api ,you can Use /get-fal or /get-fal-post for poems"}

@app.get("/get-fal")
async def get_fal_get(id: int | None = None):
    if not Hafez_Fals:
        return {"error": "No fals available."}

    if id is not None:
        fal = find_fal_by_id(id)
        if fal is None:
            return {"error": f"Fal with ID {id} not found."}
        return fal

    return random.choice(Hafez_Fals)
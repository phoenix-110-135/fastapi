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

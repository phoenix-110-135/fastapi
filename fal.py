from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
import random, json

app = FastAPI(
    title="FAL API",
    description="A simple API to get random Hafez poems",
    version="1.0.0",
)
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
        return {"error": "No fals"}

    if id is not None:
        fal = find_fal_by_id(id)
        if fal is None:
            return {"error": f"Fal with id {id} not found"}
        return fal

    return random.choice(Hafez_Fals)

@app.post("/get-fal-post/")
async def get_fal_post(request: Request):
    try:
        if not Hafez_Fals:
            return {"error": "No fals"}

        query_id = request.query_params.get("id")
        fal_id = None

        if query_id is not None:
            try:
                fal_id = int(query_id)
            except ValueError:
                return {"error": "Invalid id"}

        if fal_id is None:
            body_bytes = await request.body()
            if body_bytes:
                try:
                    body = await request.json()
                except Exception:
                    return {"error": "request body is not JSON"}

                if isinstance(body, dict) and "id" in body:
                    fal_id = body.get("id")

            if fal_id is not None:
                try:
                    fal_id = int(fal_id)
                except (ValueError, TypeError):
                    return {"error": "Invalid id"}

        if fal_id is not None:
            fal = find_fal_by_id(fal_id)
            if fal is None:
                return {"error": f"Fal with ID {fal_id} not found."}
            return fal

        return random.choice(Hafez_Fals)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "internal server Error", "detail": str(e)})
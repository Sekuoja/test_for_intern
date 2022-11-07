import uvicorn
from fastapi import FastAPI
from mongo_db import MongoDB
app = FastAPI()

db = MongoDB()

@app.get("/api/search/{text}")
async def search(text: str):
    return db.search_text(text)

@app.post("/api/delete/{id}")
async def delete_post_by_id(id: int):
    return db.delete_post(id)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
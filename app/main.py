import uvicorn
from fastapi import FastAPI
from db.db import engine
from model import task
from db.base import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI project!"}

def main():
    uvicorn.run(app,port=8000)

if __name__ == "__main__":
    main()
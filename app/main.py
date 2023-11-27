from fastapi import FastAPI

from app.routers import patients
from app.database import initialize_db

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup_event():
    initialize_db()


app.include_router(patients.router)
from fastapi import FastAPI
from app.routers import bible

app = FastAPI()

app.include_router(bible.router)

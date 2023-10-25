from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import models

from routers import users, courses
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=users.router)
app.include_router(router=courses.router)


@app.get("/")
async def root():
    return RedirectResponse('/docs')
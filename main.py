from fastapi import FastAPI

from modules.cats import cats_controller

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Woooops! Hello!"}


app.include_router(cats_controller.router)

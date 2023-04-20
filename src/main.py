from typing import Union

from src.file.router import router as file_router
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.config import DB_URL, DB_MODELS

app = FastAPI()


register_tortoise(
    app,
    db_url=DB_URL,
    modules={'models': DB_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)


app.include_router(file_router)


from tortoise.contrib.pydantic import pydantic_model_creator

from src.models import File

file_pydantic = pydantic_model_creator(File)


async def create_file(file_item):
    new_file_item = await File.create(**file_item.dict())
    # TODO: save file from request in file path and save it in DB
    return new_file_item.uuid


async def get_files():
    file_list = File.all()
    return await file_pydantic.from_queryset(file_list)


async def get_file(uuid):
    file_item = await File.get(uuid=uuid)
    return file_item

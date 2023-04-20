from typing import Annotated, Union

from fastapi import APIRouter, Depends, Header, HTTPException
from starlette.responses import FileResponse

from src import config
from src.file.schemas import FileSchema
from src.file.service import create_file, get_files, get_file


async def get_token_header(token: str | None):
    if token != config.API_TOKEN:
        raise HTTPException(status_code=403, detail='Token is invalid')


router = APIRouter(
    prefix="/api/file",
    tags=["file"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post('/')
async def upload_file(file_item: FileSchema):
    """ Получение файла для загрузки и сохранения в БД """
    file_uuid = await create_file(file_item)
    return {'status': 'ok', 'uuid': file_uuid}


@router.get('/')
async def get_file_list():
    """Получить список файлов"""
    file_list = await get_files()
    return {'status': 'ok', 'data': file_list}


async def check_token(token: Union[str, None] = None):
    if token == config.API_TOKEN:
        return True
    return False


@router.get('/{uuid}')
async def get_file_item(uuid: str, token: Annotated[str, Depends(check_token)]):
    """Получить список файлов"""
    file_item = await get_file(uuid)
    if token:
        return FileResponse(file_item.path, media_type='application/octet-stream', filename=file_item.name)
    return FileResponse(file_item.blur_path, media_type='application/octet-stream', filename=file_item.name)

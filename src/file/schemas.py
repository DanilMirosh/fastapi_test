from pydantic import BaseModel


class FileSchema(BaseModel):
    name: str
    file_type: str | None

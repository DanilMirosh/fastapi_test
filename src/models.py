from tortoise import fields
from tortoise.models import Model


class File(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    path = fields.CharField(max_length=255, null=True)
    blur_path = fields.CharField(max_length=255, null=True)  # TODO: make blur version for image file
    file_type = fields.CharField(max_length=255, null=True)  # TODO: make enum types for parsing

    def __str__(self):
        return f'{self.uuid}'

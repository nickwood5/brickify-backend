from typing import Optional
from ninja import Schema, UploadFile
from pydantic import root_validator, ValidationError

class ImageUploadSchema(Schema):
    image_file: Optional[UploadFile] = None
    image_url: Optional[str] = None

    @root_validator
    def check_image_file_or_url(cls, values):
        image_file, image_url = values.get('image_file'), values.get('image_url')
        if not image_file and not image_url:
            raise ValidationError('Either image_file or image_url must be provided.')
        return values

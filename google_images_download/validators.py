from pydantic import BaseModel, HttpUrl, validator, ValidationError
from base64 import b64decode


class ImageSrcUrl(BaseModel):
    url: HttpUrl


class ImageSrcBase64(BaseModel):
    base64_src: str

    @validator("base64_src")
    def validate_base64_src(cls, base64_src: str) -> str:
        if len(base64_src.split(",")) > 1:
            type_image, base64_src = base64_src.split(",")
        try:
            b64decode(base64_src)
            return base64_src
        except:
            raise ValidationError("Not a Valid base64 image encode")

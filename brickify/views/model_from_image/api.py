from ninja import Router, UploadedFile, File
from brickify.views.model_from_image.schemas import ImageUrlIn
from brickify.builder.builder import Builder, ImageSource
from pydantic import HttpUrl

model_from_image_router = Router()

@model_from_image_router.post("/file/")
def build_model_from_image_file(request, image_file: UploadedFile = File(...)):
    image_source_obj = ImageSource(image_file=image_file)
    Builder(image_source_obj).build()



@model_from_image_router.post("/url/")
def build_model_from_image_url(request, image_url: ImageUrlIn):
    image_source = ImageSource(image_url=image_url.image_url)
    Builder(image_source).build()
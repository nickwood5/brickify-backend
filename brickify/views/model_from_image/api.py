from ninja import Router, UploadedFile, File
from brickify.views.model_from_image.schemas import ImageUrlIn
from brickify.builder.builder import Builder, ImageSource
from pydantic import HttpUrl
from django.http import HttpResponse
from django.http import FileResponse
from uuid import uuid4

model_from_image_router = Router()

@model_from_image_router.post("/file/")
def build_model_from_image_file(request, image_file: UploadedFile = File(...)):
    image_source_obj = ImageSource(image_file=image_file)
    file_data = Builder(image_source_obj).build()

    response = HttpResponse(file_data, content_type='application/octet-stream')
    # Set the Content-Disposition header to prompt the user to save the file
    response['Content-Disposition'] = 'attachment; filename="generated_file.ldr"'

    return response


@model_from_image_router.post("/url/")
def build_model_from_image_url(request, image_url: ImageUrlIn):
    image_source = ImageSource(image_url=image_url.image_url)
    id = Builder(image_source).build()

    return {"model_id": id}


@model_from_image_router.get("/get_model/{uuid:model_id}")
def get_model(request, model_id: str):
    response = FileResponse(open(f"{model_id}.ldr", 'rb'), as_attachment=True, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{model_id}.ldr"'

    return response
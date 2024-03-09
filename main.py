from brickify.builder.builder import Builder, ImageSource
from django.core.files.uploadedfile import UploadedFile
from django.core.files import File
import io
url_image_source = ImageSource(image_url="https://image.uniqlo.com/UQ/ST3/ca/imagesgoods/466337/item/cagoods_01_466337.jpg?width=750")


with open("sample.png", 'rb') as f:
    # Create a File object (which is needed to initialize UploadedFile)
    content = f.read()

    file_like_object = io.BytesIO(content)
    file = File(file_like_object)

    uploaded_file = UploadedFile(file=file, name=file.name, content_type="image/png", size=file.size)
    

file_image_source = ImageSource(image_file=uploaded_file)

Builder(file_image_source).build()


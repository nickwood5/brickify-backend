import requests


local = "http://localhost:8000"
live = "https://brickify-backend.onrender.com"

use_local = True

if use_local:
    live = local
url = f'{live}/v1/model_from_image/url/'  # Adjust the domain as necessary



files = {
    'image_file': ('sample.png', open("sample.png", 'rb'), 'image/png'),  # Specify the MIME type here
}
data = {
    'image_url': "https://image.uniqlo.com/UQ/ST3/ca/imagesgoods/450251/item/cagoods_30_450251.jpg?width=750"
}

response = requests.post(url, json=data)
print(response.status_code, response.json())
##
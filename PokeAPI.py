from PIL import Image
from io import BytesIO
import requests, json

response = requests.get("https://pokeapi.co/api/v2/pokemon/9/")
data = json.loads(response.text)
print(data["name"])
image_url = data["sprites"]["front_shiny"]
image_data = BytesIO(requests.get(image_url).content)
image = Image.open(image_data)
image.show()


import pyjsonrpc
import base64
from PIL import Image

http_client = pyjsonrpc.HttpClient(
    url = "http://hack.israeltechallenge.com:8000",
    username = "ITC"
)

print http_client.call("help")
print http_client.call("ping")
username = 'ITC'
password = 'l33#'
message = "Hello World"
image_loc = "dig10k_penguin_enc.bmp"
print http_client.call("login", username, password)
encoded_string = ''
with open(image_loc, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

img_w_message = http_client.call("hide_message_in_image", encoded_string, message)

with open("Y.bmp", "wb") as fh:
    fh.write(base64.b64decode(img_w_message))
    fh.close()
img = Image.open("Y.bmp")
img.show()

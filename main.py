from rembg import remove
from PIL import Image
image_input = Image.open('<-- source path -->')
output = remove(image_input)
output.save('<-- destination path -->')

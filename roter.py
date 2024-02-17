from PIL import Image
from PIL import ImageFilter

im = Image.open("img.png")
im = im.transpose(Image.ROTATE_90)
im = im.convert("L")
im.save("black_white.png")
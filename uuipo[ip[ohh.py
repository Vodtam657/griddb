from PIL import Image
from PIL import ImageFilter
im =    Image.open("img.png")

print(im.format, im size, im.mode)

im.show()

filtered_image = im.filter(ImageFilter.BoxBlur(5))

filtered_image.show()

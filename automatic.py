from PIL import Image
from PIL import ImageFilter
import os

filter_list = os.listdir("photos/")

for photo_name in file_list:
    photo = Image.open("photos/"+photo_name)
    photo = photo.filter(ImageFilter.ENBOSS)
    photo.save("edited_photo/"+photo_name)
    photo.close()

print(file_list)

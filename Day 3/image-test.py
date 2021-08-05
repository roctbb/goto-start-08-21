# импортируем библиотеку
from PIL import Image

# открываем файл
img = Image.open("floppa.jpeg")

width = img.width
height = img.height

print(width, height)

y = 0
while y < height:
    x = 0
    while x < width:
        r, g, b = img.getpixel((x, y))
        r += 50
        img.putpixel((x, y), (r, g, b))
        x += 1
    y += 1

img.show()
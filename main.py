from PIL import Image

image = Image.open("ВАЗ-2101.jpg")
print("Модель", image.mode)
print("Высота", image.height)
print("Ширина", image.width)

red, green, blue = image.split()


coordinates = (24, 0, 305, 229)
red_left = red.crop(coordinates)
coordinates = (12, 0, 293, 229)
red_middle = red.crop(coordinates)
red = Image.blend(red_left, red_middle, 0.5)


coordinates = (0, 0, 281, 229)
blue_left = blue.crop(coordinates)
coordinates = (12, 0, 293, 229)
blue_middle = blue.crop(coordinates)
blue = Image.blend(blue_left, blue_middle, 0.5)


coordinates = (12, 0, 293, 229)
green = green.crop(coordinates)


new_image = Image.merge("RGB", (red, green, blue))
new_image.thumbnail((80, 80))
new_image.save("final.jpg")








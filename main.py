from PIL import Image

image = Image.open('your_image.png')
pixels = image.load()

width, height = image.size

gcx = 0
gcy = 0
sigma_i = 0

for x in range(0, width):
    for y in range(0, height):
        i = pixels[x, y][0]
        gcx += x * i
        gcy += y * i
        sigma_i += i

print(gcx / sigma_i)
print(gcy / sigma_i)

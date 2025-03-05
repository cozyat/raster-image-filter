from PIL import Image
import random
import os

if os.path.exists("raster-starter-code/newImage.jpg"):
    os.remove("raster-starter-code/newImage.jpg")

print("\n\n")

img = Image.open("raster-starter-code/image.jpg")

width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
    scale = mwidth
else:
    scale = mheight
if scale != 0:
    img = img.resize((width // scale, height // scale))

def new_filter():
    change = input("How much do you want your image to change: low, medium, or high? ")
    
    change.lower()
    location = 0

    while location < len(new_pixels):
        if change == "low":
            rand = random.randint(1, 10)
        elif change == "medium":
            rand = random.randint(11, 20)
        elif change == "high":
            rand = random.randint(21, 30)
        else:
            print("You did not choose a correct option.")
            rand = 0

        if location < len(new_pixels) - 30:
            newp = new_pixels[(location + rand) % len(new_pixels)]
        else:
            newp = new_pixels[(location - rand) % len(new_pixels)]

        nr = newp[0]
        nb = newp[1]
        ng = newp[2]

        p = new_pixels[location]

        r = p[0]
        g = p[1]
        b = p[2]

        newr = int((10 + r + nr) / 2)
        newg = int((20 + g + ng) / 2)
        newb = int((30 + b + nb) / 2)

        new_pixels[location] = (newr, newg, newb)
        location = location + 1

    newImage = Image.new("RGB", img.size)
    newImage.putdata(new_pixels)
    newImage.save("raster-starter-code/newImage.jpg")

if img.mode != "RGB":
    img = img.convert("RGB")

pixels = list(img.getdata())
new_pixels = []

for pixel in pixels:
    new_pixels.append((pixel[0], pixel[1], pixel[2]))

new_filter()

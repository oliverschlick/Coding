from PIL import Image
import os, sys

img= Image.open(r"C:\Users\hggag\Desktop\test.jpg")
width =img.size[0]
height=img.size[1]

imgr=Image.open(r"r.png")
imgg=Image.open(r"g.png")
imgb=Image.open(r"b.png")

for x in range(0,width):
    for y in range(0, height):
        pixel=(x,y)
        rgb=img.getpixel(pixel)
        print(rgb)
        break

for x in range(0,width):
    for y in range(0, height):
        pixel=(x,y)
        rgb=imgr.getpixel(pixel)
        print(rgb)
        break
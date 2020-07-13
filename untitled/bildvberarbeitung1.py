from scipy import misc
import matplotlib.pyplot as plt
import scipy.misc

face = scipy.misc.face()
print(face.shape)
print(face.max)
print(face.dtype)
plt.axis("off")
plt.gray()
plt.imshow(face)
plt.show()

image= face

def grayscale(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r,g,b = image.getpixel((x,y))
            intensity = (r+g+b) / 3
            image.putpixel( (x,y), ( intensity,intensity,intensity) )

print(image)
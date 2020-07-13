import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os, sys
img= cv.imread(r"C:\Users\hggag\Desktop\test1.jpg",0)

imgBlur=cv.GaussianBlur(cv.imread(r"C:\Users\hggag\Desktop\test1.jpg"), (7,7),1)
imgGray=cv.cvtColor(imgBlur, cv.COLOR_BGR2GRAY)

cv.imwrite(r"C:\Users\hggag\Desktop\gray.jpg", imgGray)

def main():
    r, g, b =cv.split(img)

    titles =['Original Image', 'Red', 'Green', 'Blue']
    images = [cv.merge((r, g, b)), r, g, b]

    plt.subplot(2, 2, 1)
    plt.imshow(images[0])
    plt.title(titles[0])
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2, 2, 2)
    plt.imshow(images[1], cmap='gray')
    plt.title(titles[1])
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2, 2, 3)
    plt.imshow(images[2], cmap='gray')
    plt.title(titles[2])
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2, 2, 4)
    plt.imshow(images[3], cmap='gray')
    plt.title(titles[3])
    plt.xticks([])
    plt.yticks([])

    plt.show()
"""
img1 =cv.imread(r"r.png",0)

_, th1 = cv.threshold(img1, 230, 255, cv.THRESH_BINARY)

median =cv.medianBlur(th1, 7)

kernal=np.ones((6,6), np.uint8)

opening =cv.morphologyEx(median, cv.MORPH_OPEN,kernal, iterations=1)
closing= cv.morphologyEx(opening, cv.MORPH_CLOSE, kernal, iterations=2)




def fill_holes(img):
    th1=img.copy()

    img_floodfill = th1.copy()
    h,w = th1.shape[:2]
    mask=np.zeros((h+2,w+2),np.uint8)

    if img[0,0] != 0:
        print("Warning")
    cv.floodFill(img_floodfill, mask, (0,0), 255)
    img_floodfill_inv =cv.bitwise_not(img_floodfill)

    img_out = th1 | img_floodfill_inv
    return img_out

neues_bild= fill_holes(th1)
cv.imshow("neues_bild", neues_bild)

width =img.size[0]
height=img.size[1]
white=0
black=0

print(neues_bild)
unique, counts = np.unique(neues_bild, return_counts=True)
print(dict(zip(unique, counts)))
#print("Schwarze Pixel:" +str(black), "Weiße Pixel:" +str(white))

titles = ['image', 'th1', 'median','opening', 'closing']
images =[img, th1, median, opening, closing]

for i in range(len(titles)):
    plt.subplot(3,4,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
"""

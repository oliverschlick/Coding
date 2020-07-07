from PIL import Image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os, sys
img= cv.imread(r"C:\Users\hggag\Desktop\gray.jpg",0)


imgBlur=cv.GaussianBlur(cv.imread(r"C:\Users\hggag\Desktop\test1.jpg"), (7,7),1)
imgGray=cv.cvtColor(imgBlur, cv.COLOR_BGR2GRAY)

cv.imwrite(r"C:\Users\hggag\Desktop\gray.jpg", imgGray)
"""j
data=img.getdata()
r = [(d[0], d[0], d[0]) for d in data]
g = [(d[1], d[1], d[1]) for d in data]
b = [(d[2], d[2], d[2]) for d in data]

img.putdata(r)
img.save('r.png')
img.putdata(g)
img.save('g.png')
img.putdata(b)
img.save('b.png')
"""

img1 =cv.imread(r"r.png",0)
cv.imshow("window", img)
cv.waitKey(0)


def nothing(x):
    pass

# Create a black image, a window
img2 = np.zeros((300,512,3), np.uint8)

print(type(img1))
cv.namedWindow('window')

# create trackbars for color change
cv.createTrackbar('R','window',0,255,nothing)
cv.createTrackbar('G','window',0,255,nothing)
cv.createTrackbar('B','window',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'window',0,1,nothing)

while(1):
    cv.imshow('window', img)
    k = cv.waitKey(3) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','window')
    g = cv.getTrackbarPos('G','window')
    b = cv.getTrackbarPos('B','window')
    s = cv.getTrackbarPos(switch,'window')


    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
"""
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
#cv.imshow("neues_bild", neues_bild)

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

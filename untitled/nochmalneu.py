from PIL import Image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os, sys
img= Image.open(r'C:\Users\hggag\Desktop\test2.jpg')

#imgBlur=cv.GaussianBlur(cv.imread(r"C:\Users\hggag\Desktop\test2.jpg"), (7,7),1)
#imgGray=cv.cvtColor(imgBlur, cv.COLOR_BGR2GRAY)

#cv.imwrite(r"C:\Users\hggag\Desktop\gray.jpg", imgGray)
img.save('okay.png')

data= img.getdata()
r = [(d[0], d[0], d[0]) for d in data]
g = [(d[1], d[1], d[1]) for d in data]
b = [(d[2], d[2], d[2]) for d in data]

img.putdata(r)
img.save('r.png')
img.putdata(g)
img.save('g.png')
img.putdata(b)
img.save('b.png')


img1 =cv.imread(r"b.png",0)


def nothing(x):
    pass

cv.namedWindow("Tracking")
hh='Max'
hl='Min'

wnd ='Colorbars'

cv.createTrackbar("Max", "Tracking", 0, 255, nothing)
cv.createTrackbar("Min", "Tracking", 0, 255, nothing)

img2= cv.imread('okay.png')

while(1):
    hu1=cv.getTrackbarPos("Max", "Track")
    hu2 = cv.getTrackbarPos("Max", "Track")

    ret, thresh1 =cv.threshold(img2, hu1, hu2, cv.THRESH_BINARY)
    ret, thresh2 =cv.threshold(img2, hu1, hu2, cv.THRESH_TOZERO)

    cv.imshow("thresh1", thresh1)
    cv.imshow("thresh2", thresh2)

    key=cv.waitKey(1)
    if key==27:
        break

cv.destroyAllWindows()

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


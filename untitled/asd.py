from PIL import Image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os, sys
img= Image.open(r'C:\Users\hggag\Desktop\test1.jpg')

#imgBlur=cv.GaussianBlur(cv.imread(r"C:\Users\hggag\Desktop\test2.jpg"), (7,7),1)
#imgGray=cv.cvtColor(imgBlur, cv.COLOR_BGR2GRAY)

#cv.imwrite(r"C:\Users\hggag\Desktop\gray.jpg", imgGray)
img.save('okay.png')
Img1=cv.imread(r"okay.png")
data= img.getdata()
r = [(d[0], d[0], d[0]) for d in data]
g = [(d[1], d[1], d[1]) for d in data]
b = [(d[2], d[2], d[2]) for d in data]

img.putdata(r)
img.save('r.png')
Red =cv.imread(r"r.png")
img.putdata(g)
img.save('g.png')
Green =cv.imread(r"g.png")
img.putdata(b)
img.save('b.png')
Blue =cv.imread(r"b.png")


def nothing(x):
    pass

cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)




while True:
    frame = Img1
    hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h =cv.getTrackbarPos("LH", "Tracking")
    l_s =cv.getTrackbarPos("LS", "Tracking")
    l_v =cv.getTrackbarPos("LV", "Tracking")

    u_h =cv.getTrackbarPos("UH", "Tracking")
    u_s =cv.getTrackbarPos("US", "Tracking")
    u_v =cv.getTrackbarPos("UV", "Tracking")

    l_b =np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask =cv.inRange(hsv, l_b, u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("frame",frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    key=cv.waitKey(3) & 0xFF
    if key==27:
        break

cv.destroyAllWindows()

kernal_variable= int(input("Wenn Objekt filigran, wähle kleine Zahlen zwischen 1 und 3, ansonsten auch größere:"))
kernal=np.ones((kernal_variable,kernal_variable), np.uint8)
if kernal_variable >= 4:

    median =cv.medianBlur(mask, 7)
    opening =cv.morphologyEx(median, cv.MORPH_OPEN,kernal, iterations=1)
    closing= cv.morphologyEx(opening, cv.MORPH_CLOSE, kernal, iterations=1)


elif kernal_variable <= 3:
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal, iterations=1)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernal, iterations=1)

cv.imshow("mask",mask)



"""
def fill_holes(fat):
    fat=fat.copy()

    img_floodfill = fat.copy()
    h,w = fat.shape[:2]
    mask=np.zeros((h+2,w+2),np.uint8)

    if fat[0,0] != 0:
        print("Warning")
    cv.floodFill(img_floodfill, mask, (0,0), 255)
    img_floodfill_inv =cv.bitwise_not(img_floodfill)

    img_out = fat | img_floodfill_inv
    return img_out

neues_bild= fill_holes(closing)
cv.imshow("neues_bild", neues_bild)
"""

width =img.size[0]
height=img.size[1]
white=0
black=0
cv.imshow("Closing", closing)
#print(neues_bild)
unique, counts = np.unique(closing, return_counts=True)
f=dict(zip(unique, counts))
d={'weiß':f[255], 'schwarz':f[0]}
print(d)
#print("Schwarze Pixel:" +str(black), "Weiße Pixel:" +str(white))

titles = ['image', 'mask', 'opening', 'closing']
images =[img, mask, opening, closing]

for i in range(len(titles)):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

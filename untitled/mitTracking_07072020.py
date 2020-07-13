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

titles1 = ['r.png', 'g.png', 'b.png']
images1 = [Red, Green, Blue]
for i in range(len(titles1)):
    cv.imshow(titles1[i], images1[i])
cv.waitKey(0)
cv.destroyAllWindows()

i= int(input("In which picture is the contrast the best? For r.png = 0, g.png = 1, b.png = 2:"))
img1 =images1[i]
print(images1[i])
cv.imshow(titles1[i], images1[i])
cv.waitKey(0)
cv.destroyAllWindows()
def nothing(x):
    pass

cv.namedWindow("Tracking")
cv.createTrackbar("LGray", "Tracking", 0, 255, nothing)



while True:
    frame = images1[i]
    hsv= cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    l_g =cv.getTrackbarPos("LGray", "Tracking")
    l_g1 =0
    l_g2 =0

    u_g =255
    u_g1 =255
    u_g2 =255

    l_b =np.array([l_g, l_g1, l_g2])
    u_b = np.array([u_g, u_g1, u_g2])
    mask =cv.inRange(frame, l_b, u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("frame",frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    key=cv.waitKey(3) & 0xFF
    if key==27:
        break

cv.destroyAllWindows()

Red1 =cv.imread(r"r.png",0)
Green1 =cv.imread(r"r.png",0)
Blue1 =cv.imread(r"r.png",0)
images2 = [Red1, Green1, Blue1]


_, th1 = cv.threshold(images2[i], int(input("Enter Thresholdvalue:")), 255, cv.THRESH_BINARY)

median =cv.medianBlur(th1, 7)

kernal=np.ones((6,6), np.uint8)

opening =cv.morphologyEx(median, cv.MORPH_OPEN,kernal, iterations=1)
closing= cv.morphologyEx(opening, cv.MORPH_CLOSE, kernal, iterations=2)




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

width =img.size[0]
height=img.size[1]
white=0
black=0

#print(neues_bild)
unique, counts = np.unique(neues_bild, return_counts=True)
f=dict(zip(unique, counts))
d={'weiß(0)':f[255], 'schwarz(255)':f[0]}
print(d)
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


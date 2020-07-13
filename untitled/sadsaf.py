import cv2
import numpy as np
import os

def imshow(img):
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('b.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,3,1)

_, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

mask = np.zeros(img.shape[:-1],np.uint8)

cv2.drawContours(mask,contours,-1,(255,255,255),-1)

height, width = img.shape[:-1]

mask1 = np.zeros((height+2, width+2), np.uint8)     # line 26
cv2.floodFill(mask,mask1,(0,0),255)     # line 27
mask_inv=cv2.bitwise_not(mask)

imshow(mask_inv)
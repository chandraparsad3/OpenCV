import cv2 as cv
import numpy as np

img=cv.imread('Image/dog5.jpg')
cv.imshow('Dog', img)

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

green=cv.merge([blank,g,blank])
blue=cv.merge([b,blank,blank])
red=cv.merge([blank,blank,r])

cv.imshow("Green",green)
cv.imshow("Blue",blue)
cv.imshow("Red",red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merg=cv.merge([b,g,r])
cv.imshow("Merge",merg)
cv.waitKey(0)
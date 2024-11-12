import numpy as np
import cv2 as cv

img=cv.imread('Image/dog4.jpg')
cv.imshow("Dog",img)

lap=cv.Laplacian(img,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)


soblex=cv.Sobel(img,cv.CV_64F,1,0)
sobley=cv.Sobel(img,cv.CV_64F,0,1)
combine=cv.bitwise_or(soblex,sobley)

cv.imshow('Soblex',soblex)
cv.imshow('Sobley',sobley)
cv.imshow('Combined',combine)
cv.waitKey(0)
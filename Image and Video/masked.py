import numpy as np
import cv2 as cv


img=cv.imread('Image/cat2.jpg')
cv.imshow('Image',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank",blank)

circles=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),80,255,-1)
rectangle=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+100,img.shape[0]//2+100),255,-1)

masked=cv.bitwise_and(img,img,mask=circles)
cv.imshow("Masked",masked)

masked=cv.bitwise_and(img,img,mask=rectangle)
cv.imshow("Masked",masked)


cv.waitKey(0)
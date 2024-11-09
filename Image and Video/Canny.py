import cv2 as cv
import numpy as np

img=cv.imread('Image\dog2.jpg')
cv.imshow('Cat',img)

imgs=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow("Gray",imgs)

canny=cv.Canny(img,175,250)
cv.imshow("Canny",canny)

ret,thresh=cv.threshold(imgs,125,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

# blur=cv.GaussianBlur(imgs,(5,5),cv.BORDER_CONSTANT)
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)


contours,herachries=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)  # Draws contours directly on 'blank'
cv.imshow('Contours', blank)  # Displays the modified 'blank' with contours

cv.waitKey(0)



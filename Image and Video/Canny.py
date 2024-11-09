import cv2 as cv

img=cv.imread('Image\cat3.jpg')
cv.imshow('Cat',img)

imgs=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow("Gray",imgs)


canny=cv.Canny(img,175,250)
cv.imshow("Canny",canny)
cv.waitKey(0)



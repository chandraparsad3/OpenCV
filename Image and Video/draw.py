import numpy  as np
import cv2 as cv

# pic=cv.imread('Image/cat.jpg')
# cv.imshow('Cat',pic)
# blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)


# blank[100:200 , 300:400]=0,255,0
# cv.imshow('Green',blank)

white=np.zeros((500,500,3),dtype='uint8')
cv.imshow('White',white) ## blank image.

cv.rectangle(white,(0,0),(white.shape[0]//2,white.shape[1]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow("Rectangle",white) ### displayed with greeen rectangle    

cv.circle(white,(white.shape[0]//2,white.shape[1]//2),50,(255,255,0),thickness=-1)
cv.imshow("Circle",white) ### displayed a small circle in the center 


cv.line(white,(0,0), (white.shape[0]//2,white.shape[1]//2),(125,25,125),thickness=3)
cv.imshow("Line",white) ### displayed a line 

cv.putText(white,"Hello",(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),thickness=3)
cv.imshow("Text",white) ### Hello Text displayed

cv.waitKey(0)
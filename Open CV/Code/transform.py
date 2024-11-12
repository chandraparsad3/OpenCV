import cv2 as cv
import numpy as np

img=cv.imread('Image/cat.jpg')
cv.imshow('Cat',img)
## Transform
def transform(img,x,y):
    transmat= np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimension)

imgs=transform(img,100,100)
cv.imshow('Cat',imgs)

### rotate
def rotate(img,angle,rotatepoint=None):
    (height,width)= img.shape[:2]
    if rotatepoint is None:
        rotatepoint=(height//2,width//2)

    rotmat=cv.getRotationMatrix2D(rotatepoint,angle,1.0)
    dimension=(height,width)
    return cv.warpAffine(img,rotmat,dimension)


rot=rotate(img,45)
cv.imshow('Rotate',rot)


## Flip
flip_img=cv.flip(img,1)
cv.imshow('Flip',flip_img)

cv.waitKey(0)

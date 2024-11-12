### 5 essentials opencv funtions that are mostly used 

import cv2 as cv

img=cv.imread('Image/dog1.jpg')
cv.imshow("Dog",img)

## Gray color the image

Grayimage=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",Grayimage)

## BLur

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)


### Edge Cascade

canny=cv.Canny(img,100,200)
cv.imshow("Canny",canny)



## dilated
dil=cv.dilate(img,(7,7),iterations=10)
cv.imshow('Dilated',dil)



## Eroded
ero=cv.erode(img,(7,7),iterations=10)
cv.imshow('Eroded',ero)

### resize
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resize)

### croping

crop=img[0:100, 200:300]
cv.imshow("Croped", crop)


cv.waitKey(0)

# cv.cvtColor(): Converts an image to grayscale.
# Use: Simplifies image processing, like face detection.

# cv.GaussianBlur(): Blurs an image to reduce noise and detail.
# Use: Smooths images before edge detection, like preparing for analysis in medical imaging.

# cv.Canny(): Detects edges in an image.
# Use: Identifies object boundaries, such as in autonomous vehicles for lane detection.

# cv.dilate(): Expands bright regions in an image.
# Use: Enhances features like text visibility in document processing.

# cv.erode(): Shrinks bright regions in an image.
# Use: Removes small noise, improving image quality in satellite imagery.

# cv.resize(): Resizes an image to specified dimensions.
# Use: Adapts images for different display sizes, like fitting photos for social media.

# cv.imshow(): Displays an image in a window.
# Use: Useful for debugging and visualizing image processing results during development.

# cv.crop(): Extracts a portion of the image.
# Use: Focuses on specific areas, like cropping faces from group photos for identification.
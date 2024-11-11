import numpy as np
import cv2 as cv

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(350,350),255,-1)
cv.imshow('Rectangle',rectangle)

circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Circle',circle)

bit_and=cv.bitwise_and(circle,rectangle)
cv.imshow('Bitwise and',bit_and)

bit_or=cv.bitwise_or(circle,rectangle)
cv.imshow('Bitwise or',bit_or)

bit_xor=cv.bitwise_xor(circle,rectangle)
cv.imshow('Bitwise xor',bit_xor)

bit_not=cv.bitwise_not(circle)
cv.imshow('Bitwise not',bit_not)
cv.waitKey(0)
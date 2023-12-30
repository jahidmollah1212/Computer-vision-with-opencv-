import cv2 as cv
import numpy as np

path =r'C:\Users\SDS\Downloads\357015412_885223486293891_277028376415210124_n.jpg'
img=cv.imread(path)

canny=cv.Canny(img,300,200)
# dilat image
dailat=cv.dilate(canny,np.ones((5,5),dtype=np.int8))
cv.imshow('img',img)
cv.imshow('canny',canny)
cv.imshow('dilat',dailat)
print(img.shape)
cv.waitKey(0)
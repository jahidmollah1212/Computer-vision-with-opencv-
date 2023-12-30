import cv2 as cv

path=r'C:\Users\SDS\Downloads\nature-turquoise-sea-beach-wallpaper-preview_out.jpg'

img=cv.imread(path)
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('rgb',rgb)
cv.imshow('hsv',hsv)
cv.waitKey(0)
# therer are lot of color spase

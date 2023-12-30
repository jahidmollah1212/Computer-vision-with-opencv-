import cv2 as cv
# file path
path=r'C:\Users\SDS\Downloads\nature-turquoise-sea-beach-wallpaper-preview.jpg'
# image read
img=cv.imread(path)
# image showing

cv.imshow('Image',img)
cv.waitKey(0 )
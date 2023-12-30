import cv2 as cv

path=r'C:\Users\SDS\Downloads\nature-turquoise-sea-beach-wallpaper-preview_out.jpg'


img=cv.imread(path)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# simple threshold

ret,thresh=cv.threshold(gray,120,255,cv.THRESH_BINARY)
#adaptive_threshold
th2 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
cv.imshow('th1',thresh)
cv.imshow('Thresh',th2)

cv.waitKey(0)
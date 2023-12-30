import cv2 as cv
path = r'C:\Users\SDS\Downloads\istockphoto-628334606-612x612.jpg'
img=cv.imread(path)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(gray,127,255,cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv.contourArea(cnt) < 300:
        #cv.drawContours(thresh,cnt,-1,(0,255,0),2)
        x1,y1,w,h=cv.boundingRect(cnt)
        cv.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)
#cv.imshow('img',img)
cv.imshow('thresh',img)
#cv.imshow('gray',gray)
cv.waitKey(0)
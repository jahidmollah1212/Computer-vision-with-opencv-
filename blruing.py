import cv2 as cv


path=r'C:\Users\SDS\Downloads\nature-turquoise-sea-beach-wallpaper-preview_out.jpg'
img=cv.imread(path)
# simple Blur
blur=cv.blur(img,(7,7))
gaussian=cv.GaussianBlur(img,(7,7),0)
# gaussian_blur
midean=cv.medianBlur(img,7)
# median_blur
cv.imshow('gassian',gaussian)
cv.imshow('median',midean)
cv.imshow('img',blur)
cv.waitKey(0)
import cv2 as cv

path=r'C:\Users\SDS\Pictures\shankari1.jpg'
img=cv.imread(path)
# resizin imge
resize=cv.resize(img,(400,600))
print(img.shape)
print(resize.shape)
#cv.imshow('img',img)

# crop imge
crop=resize[120:440,90:300]
cv.imshow('resize',resize)
cv.imshow('crop',crop)
cv.waitKey(0)

import cv2 as cv

path=r'C:\Users\SDS\Downloads\nature-turquoise-sea-beach-wallpaper-preview_out.jpg'

img=cv.imread(path)
resize_img=cv.resize(img,(204,340))
print('img_shape:',img.shape)
print('resize_img:',resize_img.shape)
cv.imshow('img',img)
cv.imshow('resize_img',resize_img)
cv.waitKey(0)
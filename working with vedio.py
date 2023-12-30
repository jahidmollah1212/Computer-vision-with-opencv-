import cv2 as cv
# file path
path=r'C:\Users\SDS\Downloads\carPark.mp4'
# read vedio
video=cv.VideoCapture(path)
ret= True
while ret:
    ret,frame=video.read()
    if ret:
        cv.imshow('framev',frame)
        if cv.waitKey(40) and 0xFF==ord('q'):
            break

video.release()
cv.destroyAllWindows()
import cv2 as cv
# webcam read
webcam=cv.VideoCapture(0)

# visiuliztion
while True :
    ret,frame=webcam.read()
    cv.imshow('webcam',frame)
    if cv.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()
import cv2 as cv
from PIL import Image

from unit import get_limits
yellow=[0,255,255]
cam =cv.VideoCapture(0)
while True:
    rect,frame=cam.read()

    hsv_imge=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower,upper=get_limits(color=yellow)
    mask =cv.inRange(hsv_imge,lower,upper)

    mask=Image.fromarray(mask)
    bbx=mask.getbbox()

    if bbx is not None:
        x1,x2,y1,y2=bbx
        frame=cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv.destroyAllWindows()

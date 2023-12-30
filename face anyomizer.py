import cv2 as cv
import mediapipe as mp

path=r'C:\Users\SDS\Pictures\jaml.jpg'

img=cv.imread(path)
#print(img.shape)
img=cv.resize(img,(600,600))
H,W,_=img.shape
# face detection
mp_face_detection=mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
    rgb_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    out=face_detection.process(rgb_img)

    if out.detections is not None:
        for detection in out.detections:
            location_data=detection.location_data
            bbx=location_data.relative_bounding_box

            x1,y1,w,h=bbx.xmin,bbx.ymin,bbx.width,bbx.height

            x1=int(x1*W)
            y1=int(y1*H)
            w=int(w*W)
            h=int(h*H)
            cv.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)


cv.imshow('Image',img)
cv.waitKey(0)

# save
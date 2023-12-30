import cv2 as cv
import mediapipe as mp
import numpy as np


webcam=cv.VideoCapture(0)
face_mash=mp.solutions.face_mesh
face=face_mash.FaceMesh(static_image_mode=True,min_detection_confidence=0.6,min_tracking_confidence=0.6)
draw=mp.solutions.drawing_utils

while True:
    rect,frame=webcam.read()
    rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    op=face.process(rgb)
    if op.multi_face_landmarks:
        for i in op.multi_face_landmarks:
            draw.draw_landmarks(frame,i,face_mash.FACEMESH_CONTOURS,landmark_drawing_spec=draw.DrawingSpec(color=(0,255,0),circle_radius=1))

    cv.imshow('frame',frame)

    if cv.waitKey(1)==27:
        webcam.release()
        cv.destroyAllWindows()
        break
import cv2 as cv
import mediapipe as mp

cap =cv.VideoCapture(0)
hands=mp.solutions.hands
hand=hands.Hands(static_image_mode=True,min_detection_confidence=0.6)
draw=mp.solutions.drawing_utils
while True :
    rec,frame =cap.read()
    rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    op=hand.process(rgb)
    if op.multi_hand_landmarks:
        for i in op.multi_hand_landmarks:
            draw.draw_landmarks(frame,i,hands.HAND_CONNECTIONS,landmark_drawing_spec=draw.DrawingSpec(circle_radius=2,color=(0,255,255)))


    cv.imshow('video',frame)



    if cv.waitKey(1)==27:
        cap.release()
        cv.destroyAllWindows()
        break
import numpy as np
import cv2

faceClassifier = cv2.CascadeClassifier('C:/Users/Dell/Desktop/ImageProcessing/Projects/Haar Classifiers/haar_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret = True
    while ret:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = faceClassifier.detectMultiScale(gray,1.3,4)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0),1)
        cv2.imshow("Face recognition", frame)
        if cv2.waitKey(1) == 27:
            break


cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

faceClassifier = cv2.CascadeClassifier('C:/Users/Dell/Desktop/ImageProcessing/Projects/Haar Classifiers/haar_frontalface_default.xml')
eyeClassifier = cv2.CascadeClassifier('C:/Users/Dell/Desktop/ImageProcessing/Projects/Haar Classifiers/haar_eye.xml')

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret = True
    while ret:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = faceClassifier.detectMultiScale(gray,1.3,4)
        print(faces)
        for(x,y,w,h) in faces:
            x = x-50
            y = y-50
            w = w+50
            h = h+50
            cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0),1)
            roi = gray[y:y+h,x:x+w]
            roiColor = frame[y:y+h,x:x+w]
            eyes = eyeClassifier.detectMultiScale(roi,1.2,3)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roiColor,(ex,ey), (ex+ew,ex+eh),(255,0,0),2)
            cv2.imshow("Face recognition", roiColor)
        if cv2.waitKey(1) == 27:
            break


cap.release()
cv2.destroyAllWindows()
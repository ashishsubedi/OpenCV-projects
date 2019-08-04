import numpy as np
import time
import cv2

carClassifier = cv2.CascadeClassifier('C:/Users/Dell/Desktop/ImageProcessing/Projects/Haar Classifiers/haar_cars.xml')


cap = cv2.VideoCapture("C:/Users/Dell/Desktop/ImageProcessing/video2.avi")

while cap.isOpened():

    ret,frame = cap.read()
    if(ret):
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cars = carClassifier.detectMultiScale(gray,1.2,3)

        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+w),(255,0,0),2)
        time.sleep(0.05)
        cv2.imshow("Car Detection",frame)


    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
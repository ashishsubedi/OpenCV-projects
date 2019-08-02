import cv2;
import numpy as np;

cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret = True
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    k = np.ones((7,7),np.uint8)

    while ret:

        d = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray,(7,7),0)
        ret,bin = cv2.threshold(blur,30,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(bin,k, iterations = 4)

        #opening = cv2.morphologyEx(bin, cv2.MORPH_OPEN,k)

        c, h = cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #finding and drawing contours
        for contour in c:
            if(cv2.contourArea(contour) > 1000):
                cv2.drawContours(frame1, c, -1, (255,0,0), 2)


        cv2.imshow("Original", frame1)
        cv2.imshow("Opening", dilated)


        if cv2.waitKey(1) == 27:
            break

        frame1 = frame2
        ret, frame2 = cap.read()

cv2.destroyAllWindows()
cap.release()
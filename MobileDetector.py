import cv2
import numpy as np


img = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/box.jfif", 0)

'''
    Process:
    1) Create ORB detector object
    2) Find keypoints and descriptors
    3) Create BFMatcher Object
    4) Match descriptors
    5) sort the matches and show 10 strongest matches (optional)
    6) Return no of matches
'''

def ORBMatcher(img1, img2):

    #1 + Max 1000 matches
    orb = cv2.ORB_create(1000)
    #2
    kp1,des1 = orb.detectAndCompute(img1,None)
    kp2,des2 = orb.detectAndCompute(img2,None)

    #3
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

    #4
    img3 = img1.copy()
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],img3,flags=2)
    return len(matches), img3


   
cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret = True
    while ret:
        ret, frame = cap.read()
        h,w = frame[:2]
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        topLeftX = 150;
        topLeftY = 150;
        bottomRightX = 450
        bottomRightY = 450;
        roi = frame[topLeftX:bottomRightX,topLeftY:bottomRightY]
        cv2.rectangle(frame,(topLeftX,topLeftY),(bottomRightX,bottomRightY),255,3)
       
        threshold = 170
        length,img3 = ORBMatcher(roi, img)
        print(length)
        if (length > threshold):
            outputText = "Object Detected. Match Count: " + str (length)
            cv2.putText(frame, outputText,(30,30) ,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            
        cv2.imshow("MobileDetector Using ORB", frame)
        cv2.imshow("MobileDetector Using ORB Matches", img3)
        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()
cap.release()

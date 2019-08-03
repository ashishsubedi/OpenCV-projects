import numpy as np
import cv2

img1 = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/box.jfif",0)
img2 = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/box_in_scene.png",0)


orb = cv2.ORB_create(1000);


#Find Keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)


#Create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

#Match descriptors
img3 = img2.copy()
matches = bf.match(des1,des2)

matches = sorted(matches,key= lambda x:x.distance)

#dDrawing 10 Strongmatchess
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],img3,flags=2)


cv2.imshow("Image", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
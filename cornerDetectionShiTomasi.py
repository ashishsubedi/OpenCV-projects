import cv2
import numpy as np


image = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/house.tif")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray,25,0.01,5)


corners = np.int64(corners)

for i in corners:
  
    x,y = i.ravel()
    cv2.circle(image,(x,y),3,255,-1)

cv2.imshow("image",image)
cv2.waitKey(0)

cv2.destroyAllWindows()
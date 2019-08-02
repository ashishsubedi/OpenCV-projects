import numpy as np
import cv2

'''
1) Binarize
1.5) Run Canny as findContour works on perfect edges
2) Find Contours
3) Approx Polygon
4) If length = any shape, recognized

'''
image = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/shapes.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Test",thresh)
cv2.waitKey(0)


contours, h = cv2.findContours(
    thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
contours = sorted(contours, key=cv2.contourArea, reverse=True)[1:]


for c in contours:

    # Accuracy according to perimeter of shape, check documentation
    acc = 0.011 * cv2.arcLength(c, True)
    approxCurve = cv2.approxPolyDP(c, acc, True)
    if len(approxCurve) == 3:
        cv2.drawContours(image, [c], -1, (0, 255, 0), -2)
        M = cv2.moments(c)
        if(M['m00'] != 0):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = cy = 0
        cv2.putText(image, "Triangle", (cx-20, cy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approxCurve) == 4:
        x, y, w, h = cv2.boundingRect(c)
        if(abs(w-h) >= 3):
            cv2.drawContours(image, [c], 0, (255, 0, 0), -2)
            M = cv2.moments(c)
            if(M['m00'] != 0):
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            else:
                cx = cy = 0
            cv2.putText(image, "Rectangle", (cx-20, cy),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        else:
            cv2.drawContours(image, [c], 0, (0, 0, 255), -2)
            M = cv2.moments(c)
            if(M['m00'] != 0):
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            else:
                cx = cy = 0
            cv2.putText(image, "Square", (cx-20, cy),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approxCurve) == 10:
        cv2.drawContours(image, [c], 0, (255, 255, 0), -2)
        M = cv2.moments(c)
        if(M['m00'] != 0):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = cy = 0
        cv2.putText(image, "Star", (cx-20, cy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approxCurve) >= 12:
        cv2.drawContours(image, [c], 0, (0, 255,255), -2)
        M = cv2.moments(c)
        if(M['m00'] != 0):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = cy = 0
        cv2.putText(image, "Circle", (cx-20, cy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)


    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()

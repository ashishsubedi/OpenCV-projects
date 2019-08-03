import cv2
import numpy as np
img = cv2.imread("C:/Users/Dell/Desktop/ImageProcessing/sudoku.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 120, 150)

lines = cv2.HoughLines(edges, 1, np.pi/180, 250)
for index,line in enumerate(lines):
    for r, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)

        x0 = a*r
        y0 = b*r

        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000*a)
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000*a)

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 5)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

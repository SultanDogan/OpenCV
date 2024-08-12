#Renk uzayının degistirilmesi

import cv2 as cv

#HSV  : hue saturation value ,nenelerin takibini kolaylaştırır

img = cv.imread("opencv_logo.png")
cv.namedWindow("rgb",cv.WINDOW_AUTOSIZE)
cv.imshow("rgb",img)
cv.waitKey(0)

#RGB to GRAY
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

#HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)
cv.waitKey(0)

cv.destroyAllWindows()
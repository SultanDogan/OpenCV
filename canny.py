# Canny edge detection : Bu da en popüler kenar hesaplamalardan biri

import cv2 as cv
import numpy as np

src = cv.imread("opencv_logo.png")
cv.imshow("input",src)
cv.waitKey(0)

edge=cv.Canny(src,100,300)
cv.imshow("edge",edge)
cv.waitKey(0)

cv.destroyAllWindows()

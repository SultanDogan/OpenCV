# ROI (Region of interest)

import cv2 as cv

src = cv.imread("opencv_logo.png")

h,w = src.shape[:2]

img= src.copy()

roi = img[100:250,50:300,:]

roi.shape[:2]

cv.imshow("roi",roi)
cv.waitKey(0)

img[0:150,0:250,:]= roi
cv.imshow("img",img)
cv.waitKey(0)

res = cv.resize(roi,None,fx=0.3,fy=0.3,interpolation=cv.INTER_CUBIC)
cv.imshow('res',res)
cv.waitKey(0)

res.shape[:2]

img[0:45,0:75,:]= res
cv.imshow("img",img)
cv.waitKey(0)

src[0:45,0:75,:]= res
cv.imshow("img",src)
cv.waitKey(0)

cv.destroyAllWindows()
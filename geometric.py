import cv2 as cv
import numpy as np

# shifting

img = cv.imread("opencv_logo.png")

rows= img.shape[0]
cols=img.shape[1]

M = np.float32([[1,0,300],[0,1,90]])

shifted = cv.warpAffine(img,M,(cols,rows))

cv.imshow('orginal',img)
cv.waitKey(0)

cv.imshow('shifted',shifted)
cv.waitKey(0)

# rotation

M = cv.getRotationMatrix2D((cols/2,rows/2),90,1)

dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow("img",dst)
cv.waitKey(0)

# scaling

res = cv.resize(img,None, fx=0.2,fy=0.2,interpolation=cv.INTER_CUBIC)
cv.imshow("img",res)
cv.waitKey(0)


# kucuk resim
rows= res.shape[0]
cols=res.shape[1]

M = np.float32([[1,0,200],[0,1,90]])
shifted = cv.warpAffine(res,M,(cols,rows))
cv.imshow('orginal',res)
cv.waitKey(0)

shifted = cv.warpAffine(res,M,(cols,rows))
cv.imshow('shifted',shifted)
cv.waitKey(0)

M = cv.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv.warpAffine(res,M,(cols,rows))
cv.imshow("img",dst)
cv.waitKey(0)


cv.destroyAllWindows()
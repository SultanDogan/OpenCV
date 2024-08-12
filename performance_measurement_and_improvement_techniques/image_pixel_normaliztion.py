#Image pixel normalization

import cv2 as cv
import numpy as np

path = "opencv_logo.png"

src = cv.imread(path)

print(src.shape)

gray= cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

print(gray.shape)
print(gray)

gray = np.float32(gray)
print(gray)

#Norm_minMax

min_value,max_value,min_loc,max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value,max_value))

means,stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means,stddev))

dst = np.zeros(gray.shape,dtype=np.float32)

cv.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv.NORM_MINMAX)
print(dst)

print(np.uint8(dst*255))

means,stddev = cv.meanStdDev(np.uint8(dst*255))
print("mean: %.2f, stddev: %.2f" % (means,stddev))

cv.imshow("norm_minmax",dst)
cv.waitKey(0)

min_value,max_value,min_loc,max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_value,max_value))

means,stddev = cv.meanStdDev(dst)
print("mean: %.2f, stddev: %.2f" % (means,stddev))

cv.imshow("norm_minmax",np.uint8(dst*255))
cv.waitKey(0)

cv.destroyAllWindows()

### NORM_INF ###

dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=1.0,beta=0,norm_type=cv.NORM_INF)
print(dst)
cv.imshow("norm_inf",np.uint8(dst*255))
cv.waitKey(0)

### NORM_L2 ###
dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=1.0,beta=0,norm_type=cv.NORM_L2)
print(dst)
cv.imshow("norm_l2",np.uint8(dst*10000))
cv.waitKey(0)

cv.destroyAllWindows()
#PERFORMANS OLCME VE GELISTIRME TEKNIKLERI

#Image pixel value statistics

import cv2 as cv
import numpy as np

path = "../opencv_logo.png"

src= cv.imread(path,cv.IMREAD_GRAYSCALE)

#minMaxLoc
min_value,max_value,min_loc,max_loc =cv.minMaxLoc(src)
print("min_value: %.2f,max_value: %.2f" % (min_value,max_value))

print("min_loc:",min_loc,",","max_loc:",max_loc)

#meanStdDev
means,stddev=cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f" %  (means,stddev))

src[np.where(src<means)]=0
src[np.where(src>means)]=255

cv.imshow("binary",src)
cv.waitKey(0)

cv.destroyAllWindows()


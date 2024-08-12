#MERGING TWO IMAGES

import cv2 as cv
import numpy as np

path1= "opencv_logo.png"
path2 = "opencv_logo.pnggray.png"

img1= cv.imread(path1)
img2 =cv.imread(path2)

cv.imshow("img1",img1)
cv.waitKey(0)

cv.imshow("img2",img2)
cv.waitKey(0)

horizontal=np.hstack((img2,img1))
cv.imshow("merged_images",horizontal)
cv.waitKey(0)

cv.destroyAllWindows()
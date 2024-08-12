# Load Image

# !pip install opencv-python

import cv2 as cv

path = "opencv_logo.png"

img = cv.imread(path)
type(img)

# namedWindow
cv.namedWindow("opencv_test",cv.WINDOW_AUTOSIZE)

#imshow
cv.imshow("opencv_test",img)
cv.waitKey(0)

cv.destroyAllWindows()
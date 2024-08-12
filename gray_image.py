#Gray Image

import cv2 as cv

path = "opencv_logo.png"

img = cv.imread(path)
cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored",img)
cv.waitKey(0)

#cvtColor
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

#imwrite
cv.imwrite(path + "gray.png",gray)
cv.destroyAllWindows()

#resmi dönüştürmeden direk gri okumak için
img = cv.imread(path,cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray",cv.WINDOW_AUTOSIZE)
cv.imshow("gray",img)
cv.waitKey(0)

cv.destroyAllWindows()
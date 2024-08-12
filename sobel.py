# Sobel operator = kenar algılama için en çok kullanılan yöntem(türev kullanıyor)
#x ve y eksenlerine göre görüntünün türevini alıyor.

import cv2 as cv
import numpy as np

src = cv.imread("opencv_logo.png")

h, w = src.shape[:2]

x_grad=cv.Sobel(src,cv.CV_32F,1,0)
y_grad=cv.Sobel(src,cv.CV_32F,0,1)

x_grad=cv.convertScaleAbs(x_grad)
y_grad=cv.convertScaleAbs(y_grad)

cv.imshow("x_grad",x_grad)
cv.waitKey(0)

cv.imshow("y_grad",y_grad)
cv.waitKey(0)

dst=cv.add(x_grad,y_grad,dtype=cv.CV_16S)
dst=cv.convertScaleAbs(dst)

cv.imshow("dst",dst)
cv.waitKey(0)

cv.destroyAllWindows()

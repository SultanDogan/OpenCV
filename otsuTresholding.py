# Otsu Thresholding
# Görüntü piksellerinin eşik değerine göre siyah ya da beyaz olarak güncellenmesi işlemini yapar.

import cv2 as cv
import numpy as np

src = cv.imread("opencv_logo.png")
cv.imshow("input",src)
cv.waitKey(0)

gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)

ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)

h,w=src.shape[:2]

cv.imshow("binary",binary)
cv.waitKey(0)

cv.destroyAllWindows()

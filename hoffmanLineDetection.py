# Hoffman Line Detection

#Sudoku resmi üzerindeki ızgara
#şeklindeki hücrelerin çizgilerinin tespiti hoffman yöntemi ile ele alınmıştır.

import cv2 as cv
import numpy as np

def canny_demo(image):
    t=100
    canny_output=cv.Canny(image,t,t*2)
    cv.imshow("canny_output",canny_output)
    return canny_output

src=cv.imread("opencv_logo.png")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

binary=canny_demo(src)
cv.imshow("binary",binary)
cv.waitKey(0)

lines = cv.HoughLines(binary,1,np.pi/180,150,None,0,0)

if lines is not None:
    for i in range(0,len(lines)):
        rho=lines[i][0][0]
        theta=lines[i][0][0]
        a = np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho
        pt1=(int(x0+1000*(-b)),int(y0+1000*(a)))
        pt2=(int(x0-1000*(-b)),int(y0-1000*(a)))
        cv.line(src,pt1,pt2,(0,0,255),3,cv.LINE_AA)

cv.destroyAllWindows()
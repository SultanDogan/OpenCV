# Probability hoffman line detection
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

binary = canny_demo(src)
cv.imshow("binary",binary)
cv.waitKey(1)

lineP = cv.HoughLinesP(binary,1,np.pi/180,55,None,50,10)
cv.HoughLinesP
if lineP is not None:
    for i in range(0,len(lineP)):
        l=lineP[i][0]
        cv.line(src,(l[0],l[1]),(l[2],l[3]),(255,0,0),1,cv.LINE_AA)

cv.imshow("hough line demo",src)
cv.waitKey(0)

cv.destroyAllWindows()
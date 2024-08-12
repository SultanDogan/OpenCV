import cv2 as cv

src1 = cv.imread("opencv_logo.png")
src2 = cv.imread("opencv_logo.pnggray.png")

#cvtColor
hsv1 = cv.cvtColor(src1,cv.COLOR_BGR2HSV)
hsv2=cv.cvtColor(src2,cv.COLOR_BGR2HSV)

#calcHist
hist1=cv.calcHist([hsv1],[0,1],None,[60,64],[0,180,0,256])
hist2=cv.calcHist([hsv2],[0,1],None,[60,64],[0,180,0,256])

#normalize
cv.normalize(hist1,hist1,0,1.0,cv.NORM_MINMAX)
cv.normalize(hist2,hist2,0,1.0,cv.NORM_MINMAX)

#compareHist

#yöntemler: HISTCMP_CORREL , HISTCMP_CHISQR vs.

#HISTCMP_CORREL

cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL) # -1 , 1 arası değerler alır 1 e yaklaştıkça
#corelasyon yani benzerlik artar...
cv.destroyAllWindows()
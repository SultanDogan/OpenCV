#Video Read Write

import cv2 as cv
import numpy as np

capture = cv.VideoCapture("video.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width= capture.get(cv.CAP_PROP_FRAME_WIDTH)
count= capture.get(cv.CAP_PROP_FRAME_COUNT)
fps=capture.get(cv.CAP_PROP_FPS)
print(height,width,count,fps)

out = cv.VideoWriter("video.avi",
                     cv.VideoWriter_fourcc('D','I','V','X'),15,
                     (np.int(width),np.int(height)),True)

while True:
    #kameradan goruntu al
    ret,frame = capture.read()

    #görüntü başarıyla alındı mı kontrol et
    if ret is True:
        #okunan görüntüyü ekranda göster
        cv.imshow("video input",frame)
        out.write(frame)
        #50 sn sonra çık
        c = cv.waitKey(50)
        if c == 27: #ESC
            break
    else:
        break
capture.release()
out.release()


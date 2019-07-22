import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #一帧一帧的捕捉视频
    ret, frame = cap.read()

    #捕捉完视频帧之后我们可以对它进行一些操作
    resultFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #展示处理之后的视频帧
    cv2.imshow('frame',resultFrame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

#最后记得释放捕捉
cap.release()
cv2.destroyAllWindows()
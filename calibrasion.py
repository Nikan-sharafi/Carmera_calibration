import cv2
import numpy as np


x,y=float(input('x:')),float(input('y:'))
parametr=cv2.aruco.DetectorParameters_create()
aruco_dict=cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    corners,_,_=cv2.aruco.detectMarkers(img,aruco_dict,parameters=parametr)
    int_corners=np.intp(corners)
    cv2.polylines(img,int_corners,True,(0,255,0),5)
    h=y
    w=x

    if corners:
        aruco_parametr=cv2.arcLength(corners[0],True)
        px_to_cm=aruco_parametr /20
        w/=px_to_cm
        h/=px_to_cm
        cv2.putText(img, f'Width {round(w,1)}', (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.putText(img, f'Height {round(h,1)}', (100, 130), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


    pts=np.array([[x,y]],np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img,pts,True, (0, 0, 255), 30)

    cv2.imshow('img',img)
    cv2.waitKey(1)
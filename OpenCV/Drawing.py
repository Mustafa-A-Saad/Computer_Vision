import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 = 1 webcam

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) # width of frame  # default is float, that's why we use int
    height = int(cap.get(4)) # height of frame

    img = cv2.line(frame , (0,0), ( width , height ),(255,0,0), 10)
    img = cv2.line(img , (0,height), ( width , 0 ),(0,255,0), 5)
    img = cv2.rectangle(img, (100,100) , (200,200) , (128,128,128) , -1 ) # -1 fill the entire thing
    img = cv2.circle(img, (300,300) , 60 , (0,0,255),-1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img,"Tefa is good!", (10,height - 10) , font,1 ,(0,0,0),5,cv2.LINE_AA)

    cv2.imshow('frame', img)  # Display the composite image 'image' instead of 'frame'
    if cv2.waitKey(1) == ord('q'): # press q to end the video capturing  # ord = ASCII Code
        break
cap.release()
cv2.destroyAllWindows()

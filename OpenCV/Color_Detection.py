import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 = 1 webcam

# RGB = Red Green Blue
# BGR : Blue Green Red
# HSV : Hue Saturation Vibrance

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) # width of frame  # default is float, that's why we use int
    height = int(cap.get(4)) # height of frame

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    light_blue = np.array([90,50,50]) # HSV color picker
    dark_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,light_blue,dark_blue) # all pixels that isn't in the range of light and dark blue will go black or white
    result = cv2.bitwise_and(frame,frame,mask=mask)


    cv2.imshow('frame', result)  # Display the composite image 'image' instead of 'frame'
    cv2.imshow('mask', mask)  # Display the composite image 'image' instead of 'frame'

    if cv2.waitKey(1) == ord('q'): # press q to end the video capturing  # ord = ASCII Code
        break
cap.release()
cv2.destroyAllWindows()

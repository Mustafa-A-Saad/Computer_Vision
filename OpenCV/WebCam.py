import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 = 1 webcam

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) # width of frame  # default is float, that's why we use int
    height = int(cap.get(4)) # height of frame

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)        # Top Left
    image[height // 2: , :width // 2] = smaller_frame   # Bottom Left
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)        # Top right
    image[height // 2: , width // 2:] = smaller_frame       # Bottom Right

    cv2.imshow('frame', image)  # Display the composite image 'image' instead of 'frame'
    if cv2.waitKey(1) == ord('q'): # press q to end the video capturing  # ord = ASCII Code
        break
cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2

img = cv2.imread('imgs/chessboard.png',)

img = cv2.resize(img,(0,0),fx=0.75,fy=0.75)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # for corner dectection works better for grayscale , don't use flags

corners = cv2.goodFeaturesToTrack(gray,100,0.01,10) # will return 100 corners # qualitylevel is like a score , the less number the less accuary
corners = np.intp(corners) # our first corner is float so we change to integer

for corner in corners:
    # print(corner) # a list of 3d arrays
    x,y = corner.ravel()   # ravel = flatten = [[1 , 2] , [2 , 1]] -> [1,2,2,1]
    cv2.circle(img,(x,y),5,(255,0,0),-1)

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('imgs\\logo.jpg',-1)

# -1 , cv2.IMREAD_COLOR # loads a color image. any trasnparency of image will be neglected. it is the deafult flag.
# 0 , cv2.IMREAD_GRAYSCALE # loads image in grayscale mode
# 1 , cv2.IMREAD_UNCHANGED # loads image as such including alpha channel

plt.imshow(img)

# cv2.imshow('image',img)
# cv2.waitKey(0) # 0 wait infinite time till hit a key , if u did 5 , then it will wait 5 seconds till a key is pressed otherwise skipped
# cv2.destroyAllWindows

# use in pycharm

img = cv2.resize(img, (400,400))

plt.imshow(img)

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
plt.imshow(img)

cv2.imwrite('new_img.jpg',img)

#-------Fundementals--------#

img = cv2.imread('imgs/logo.jpg')

img.shape
# ( height , width , channels)
# channel is color space like RGB

img.shape[1] # the width

import random

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

# you can change colors for a certain part

plt.imshow(img)

# cv2.imshow('Image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# used in pycharm

tag = img[350:500, 350:600]
img[100:250,650:900] = tag

# replacing a piece with another piece

plt.imshow(img)


import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt

def nothing(x):
    pass

img = cv.imread('mina.jpg', 0)

# edges = cv.Canny(img,100,200)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()

switch = 'OFF / ON'
cv.namedWindow('canny')
cv.createTrackbar(switch, 'canny', 0, 1, nothing)
cv.createTrackbar('Lower', 'canny', 0, 255, nothing)
cv.createTrackbar('Upper', 'canny', 0, 255, nothing)

while(True):
    Lower = cv.getTrackbarPos('Lower', 'canny')
    Upper = cv.getTrackbarPos('Upper', 'canny')
    s = cv.getTrackbarPos(switch, 'canny')

    if s == 0:
        edges = img
    else:
        edges = cv.Canny(img, Lower, Upper)
    cv.imshow('canny', edges)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
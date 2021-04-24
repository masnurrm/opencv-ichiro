import numpy as np
import cv2 as cv
img = cv.imread('wendy.jpg', 1)
res = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv.resize(img, (1*width, 1*height), interpolation = cv.INTER_CUBIC)


cv.imshow('image scalling', res)
cv.waitKey()
cv.destroyAllWindows()
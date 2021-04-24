import cv2 as cv
import numpy as np

img = cv.imread('ryujin.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

cv.imshow('erosion', opening)
cv.waitKey(0)
cv.destroyAllWindows()
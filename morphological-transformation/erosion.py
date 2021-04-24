import cv2 as cv
import numpy as np

img = cv.imread('ryujin.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations = 1)

cv.imshow('erosion', erosion)
cv.waitKey(0)
cv.destroyAllWindows()
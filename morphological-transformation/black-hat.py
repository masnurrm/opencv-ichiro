import cv2 as cv
import numpy as np

img = cv.imread('ryujin.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow('erosion', blackhat)
cv.waitKey(0)
cv.destroyAllWindows()
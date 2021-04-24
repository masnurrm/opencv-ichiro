import cv2 as cv
import numpy as np

img = cv.imread("wendy.jpg", 0)
height = img.shape[1]
width = img.shape[0]

cv.line(img, (height, width), (0,0), (255, 100, 100), 3)

cv.imshow('draw', img)
cv.waitKey(0)
cv.destroyAllWindows()
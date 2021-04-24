import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('mina.jpg')
kernel = np.ones((5,5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.show()
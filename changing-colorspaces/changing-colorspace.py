import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    lower_red = np.array([0, 100, 85])
    upper_red = np.array([30, 255, 255])

    lower_green = np.array([60, 100, 70])
    upper_green = np.array([100, 255, 255])

    lower_rgb = np.array([0, 80, 80])
    upper_rgb = np.array([130, 255, 255])
    
    
    # Threshold the HSV image to get only blue colors
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    mask_rgb = cv.inRange(hsv, lower_rgb, upper_rgb)

    # Bitwise-AND mask and original image
    res_blue = cv.bitwise_and(frame, frame, mask = mask_blue)
    res_red = cv.bitwise_and(frame, frame, mask = mask_red)
    res_green = cv.bitwise_and(frame, frame, mask = mask_green)
    res_rgb = cv.bitwise_and(frame, frame, mask = mask_rgb)
    res_bgr = res_blue + res_green + res_red

    # cv.imshow('blue', res_blue)
    # cv.imshow('red', res_red)
    # cv.imshow('green', res_green)
    cv.imshow('normal', frame)
    # cv.imshow('RGB', res_rgb)
    cv.imshow('BGR', res_bgr)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()

# CHECKING HSV OF ONE COLOR (example:green)
# import cv2 as cv
# import numpy as np
# green = np.uint8([[[0,255,0 ]]])
# hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
# print( hsv_green )

# blue = np.uint8([[[255,0,0 ]]])
# hsv_blue = cv.cvtColor(blue,cv.COLOR_BGR2HSV)
# print( hsv_blue )

# red = np.uint8([[[0,0,255 ]]])
# hsv_red = cv.cvtColor(red,cv.COLOR_BGR2HSV)
# print( hsv_red )



# experimented_code SKIN
# lower_blue = np.array([50, 50, 50])
# upper_blue = np.array([130, 255, 255])

# BLUE
# np.array([100, 50, 50])
# upper_blue = np.array([130, 200, 200])

# lower_blue = np.array([100, 50, 50])
# upper_blue = np.array([130, 255, 255])

# Using https://alloyui.com/examples/color-picker/hsv.html
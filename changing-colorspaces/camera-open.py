import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow('video', frame)
    if cv.waitKey(1) == ord('q'):
        breakpoint

cap.release()
cv.destroyAllWindows()
import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0) 

while(1): 
	
	_, frame = cap.read() 

	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 

	red_lower = np.array([0, 100, 85]) 
	red_upper = np.array([30, 255, 255]) 
	red_mask = cv.inRange(hsv, red_lower, red_upper) 

	green_lower = np.array([60, 100, 70]) 
	green_upper = np.array([100, 255, 255]) 
	green_mask = cv.inRange(hsv, green_lower, green_upper) 

	blue_lower = np.array([100, 100, 100]) 
	blue_upper = np.array([130, 255, 255]) 
	blue_mask = cv.inRange(hsv, blue_lower, blue_upper) 
	
	kernal = np.ones((5, 5), "uint8") 
	
	red_mask = cv.dilate(red_mask, kernal) 
	res_red = cv.bitwise_and(frame, frame, mask = red_mask) 
	
	green_mask = cv.dilate(green_mask, kernal) 
	res_green = cv.bitwise_and(frame, frame, mask = green_mask) 

	blue_mask = cv.dilate(blue_mask, kernal) 
	res_blue = cv.bitwise_and(frame, frame, mask = blue_mask) 

	# Creating contour to track red color 
	contours, hierarchy = cv.findContours(red_mask, 
										cv.RETR_TREE, 
										cv.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv.boundingRect(contour) 
			frame = cv.rectangle(frame, (x, y), 
									(x + w, y + h), 
									(0, 0, 255), 2) 
			
			cv.putText(frame, "Merah", (x, y), 
						cv.FONT_HERSHEY_SIMPLEX, 1.0, 
						(0, 0, 255))	 

	# Creating contour to track green color 
	contours, hierarchy = cv.findContours(green_mask, 
										cv.RETR_TREE, 
										cv.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv.boundingRect(contour) 
			frame = cv.rectangle(frame, (x, y), 
									(x + w, y + h), 
									(0, 255, 0), 2) 
			
			cv.putText(frame, "Hijau", (x, y), 
						cv.FONT_HERSHEY_SIMPLEX, 
						1.0, (0, 255, 0)) 

	# Creating contour to track blue color 
	contours, hierarchy = cv.findContours(blue_mask, 
										cv.RETR_TREE, 
										cv.CHAIN_APPROX_SIMPLE) 
                                        
	for pic, contour in enumerate(contours): 
		area = cv.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv.boundingRect(contour) 
			frame = cv.rectangle(frame, (x, y), 
									(x + w, y + h), 
									(255, 0, 0), 2) 
			
			cv.putText(frame, "Biru", (x, y), 
						cv.FONT_HERSHEY_SIMPLEX, 
						1.0, (255, 0, 0)) 
			
	# Program Termination 
	cv.imshow("RGB", frame) 
	if cv.waitKey(10) & 0xFF == ord('q'): 
		cap.release() 
		cv.destroyAllWindows() 
		break
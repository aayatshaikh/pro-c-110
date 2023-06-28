# To Capture Frame
import cv2

# To process image array
import numpy as np


# import the tensorflow modules and load the model

import tenserflow as tf

# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:

		# Flip the frame
		frame = cv2.flip(frame , 1)
		
		
		
		#resize the frame
		resized_frame = cv2.resize(frame, (desired_width, desired_height))
		
		# expand the dimensions
		expanded_frame = np.expand_dims(frame, axis=0)
		
		# normalize it before feeding to the model
		normalized_image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
		# get predictions from the model
		predictions = model.predict(input_data)
		
		
		# displaying the frames captured
		cv2.imshow('feed' , frame)

		# waiting for 1ms
		code = cv2.waitKey(1)
		
		# if space key is pressed, break the loop
		if code == 32:
			break

# release the camera from the application software
camera.release()

# close the open window
cv2.destroyAllWindows()

'''Like a series of waterfalls, the OpenCV cascade breaks the problem of detecting faces into multiple stages. For each block, it does a very rough and quick test. If that passes, it does a slightly more detailed test, and so on. The algorithm may have 30-50 of these stages or cascades, and it will only detect a face if all stages pass. The advantage is that the majority of the pictures will return negative during the first few stages, which means the algorithm won’t waste time testing all 6,000 features on it. Instead of taking hours, face detection can now be done in real time.'''

import cv2
import sys


#creating a face cascade
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

#sets the video source to the default webcam, which OpenCV can easily capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read() #read() function reads one frame from the video source. Returns The actual video frame read (one frame on each loop) and a return code
    #The return code tells us if we have run out of frames, which will happen if we are reading from a file. This doesn’t matter when reading from the webcam, since we can record forever, so we will ignore it.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #read the image and convert it to grayscale

    faces = faceCascade.detectMultiScale( #detectMultiScale function is a general function that detects objects. Since we are calling it on the face cascade, that’s what it detects. The first option is the grayscale image.
        gray,
        scaleFactor=1.1, #Since some faces may be closer to the camera, they would appear bigger than those faces in the back. The scale factor compensates for this.
        minNeighbors=5, #The detection algorithm uses a moving window to detect objects. minNeighbors defines how many objects are detected near the current one before it declares the face found. minSize, meanwhile, gives the size of each window
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    #The function returns a list of rectangles where it believes it found a face. Next, we will loop over where it thinks it found something.
    #This function returns 4 values: the x and y location of the rectangle, and the rectangle’s width and height (w , h).
	#We use these values to draw a rectangle using the built-in rectangle() function.
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #q to quit
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
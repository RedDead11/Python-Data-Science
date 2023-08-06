import cv2 as cv

# Load the pre-trained cascade classifier for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

capture = cv.VideoCapture(0)  # Use 0 to capture from the default camera

# Set the desired speedup factor
speedup_factor = 2  # Increase this value to speed up the video

while True:
    isTrue, frame = capture.read()
    
    # Check if the frame was read successfully
    if not isTrue:
        break

    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('Video', frame)
    
    # Adjust the delay based on the speedup factor
    delay = int(1000 / (capture.get(cv.CAP_PROP_FPS) * speedup_factor))

    if cv.waitKey(delay) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
